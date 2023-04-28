from django.shortcuts import render, redirect
# from django.db.models import F
from .models import TodoList, ListItem
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse

# from django.template import RequestContext

# Create your views here.
def index(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        picture = request.FILES.get("picture")
        if len(title) > 0 and len(description) > 0 and picture is not None:
            todo_list = TodoList(title = title, description = description, picture = picture)
            todo_list.save()
            return redirect("home")
        else:
            messages.info(request, "Complete All Fields")
            return redirect("home")
    return render(request, "index.html")

    #     form = TodoListCreate(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("home")
    # else:
    #     form = TodoListCreate()
    #     return render(request, "index.html", {"form":form})

    # lists = TodoList.objects.all()
    # context = {'lists': lists}
    # return render(request, 'index.html')

def edit_todolist(request, pk):
    todo_list = TodoList.objects.get(pk = pk)
    form = TodoListForm(instance=todo_list)

    if request.method == 'POST':
        form = TodoListForm(request.POST, instance=todo_list)
        if form.is_valid:
            form.save()
            return redirect("home")
    context = {'todo_list': todo_list, 'form': form}
    return render(request, 'edit-list.html', context)

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def detail(request, pk):
    todo_list = TodoList.objects.get(pk = pk) 
    list_items = todo_list.list_items.all() # 2nd Option (Reverse Relationship).
    list_item = todo_list.list_items.filter(item_list = todo_list.pk)
    # list_items = todo_list.listitem_set.all() # 1st Option (Reverse Relationship). Write the ListItem model in small letter followed by "_set". 
    # data = {}
    # form = ListItemForm()
    # if request.method == 'POST':
    # if request.is_ajax():
    # if is_ajax(request=request):
    #     if form.is_valid:
    #         form.save()
    #         data['item_name'] = form.cleaned_data.get('item_name')
    #         data['status'] = 'ok'
    #         return JsonResponse(data)
    context = {
        "todo_list": todo_list,
        "list_items": list_items,
        "list_item": list_item,
    }
    if request.method == 'POST':
        list_item.delete()
        return redirect('detail', context)
    else:
        return render(request, 'detail.html', context)

    # return render(request, 'detail.html', context)
def new_item(request, pk):
    todo_list = TodoList.objects.get(pk = pk) 
    # list_items = todo_list.list_items.all() # 2nd Option (Reverse Relationship).
    list_items = todo_list.list_items.filter(item_list = todo_list.pk)
    list_item = None
    if request.method == 'POST':
        form = ListItemForm(request.POST)
        if form.is_valid:
            list_item = form.save(commit=False)
            list_item.item_name = todo_list
            list_item.save()
            return redirect("new_item")
    else:
        form = ListItemForm()
        return render(request, "new-item.html", {"form": form,})

    # forms.fields['todo_list'].initial = "{{todo_list.pk}}"

def get_items(request, pk):
    todo_list = TodoList.objects.get(pk = pk) 
    list_items = todo_list.list_items.all() # 2nd Option (Reverse Relationship).
    return JsonResponse({"list_items": list(list_items.values())})

# def new_item(request):
#     if request.method == "POST":
#         item_name = request.POST["item_name"]
#         item_list = request.POST["item_list"]
#         # completed = request.POST["completed"]

#         form = ListItemForm(request.POST)
#         if form.is_valid:
#             form.save()
#         # new_list_item = ListItem(item_name=item_name, item_list=item_list)
#         # new_list_item.save()
#         return HttpResponse("New Item Added")

        # '''
        # todo_list = TodoList.objects.get(pk=pk) 
        # # list_items = todo_list.listitem_set.all() # 1st Option (Reverse Relationship). Write the ListItem model in small letter followed by "_set". 
        # list_items = todo_list.list_items.all() # 2nd Option (Reverse Relationship).
        # context = {
        #     "todo_list": todo_list,
        #     "list_items": list_items
        # }
        # '''

def delete(request, pk):
    todo_list = TodoList.objects.get(pk = pk) 
    if request.method == 'POST':
        todo_list.delete()
        return redirect('home')
    else:
        # messages.info(request, "Are you sure?", {"todo_list": todo_list})
        return render(request, 'delete-list.html', {"todo_list": todo_list})

def deleted(request, pk):
    todo_list = TodoList.objects.get(pk = pk) 
    return render(request, "deleted.html", {"todo_list": todo_list})

