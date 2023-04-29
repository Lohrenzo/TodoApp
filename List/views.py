from django.shortcuts import render, redirect, get_object_or_404
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
    # list_items = todo_list.list_items.all() # 2nd Option (Reverse Relationship).
    list_items = todo_list.list_items.filter(item_list = todo_list.pk)
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

    list_item = None
    if request.method == 'POST':
        item_form = ListItemForm(request.POST)
        if item_form.is_valid:
            list_item = item_form.save(commit=False)
            list_item.item_list = todo_list
            list_item.save()
            return redirect("detail", pk=pk)
    else:
        item_form = ListItemForm()
    context = {
        "todo_list": todo_list,
        "list_items": list_items,
        "list_item": list_item,
        "item_form": item_form
    }
    return render(request, "detail.html", context)

def delete_list_item(request, list_pk, item_pk):
    todo_list = TodoList.objects.get(pk = list_pk) 
    # list_items = todo_list.list_items.filter(item_list = todo_list.pk)
    list_item = get_object_or_404(ListItem, pk = item_pk)

    # Make sure the item to delete is part of the parent list
    if list_item.todo_list != todo_list:
        return redirect("detail", pk = list_pk)
    
    if request.method == 'POST':
        list_item.delete()
        return redirect('detail', pk = list_pk)
    
    return render(request, 'delete-list-item.html', {
        "list_item": list_item,
        "todo_list": todo_list
        })

# def get_items(request, pk):
#     todo_list = TodoList.objects.get(pk = pk) 
#     list_items = todo_list.list_items.all() # 2nd Option (Reverse Relationship).
#     return JsonResponse({"list_items": list(list_items.values())})

def delete(request, pk):
    todo_list = TodoList.objects.get(pk = pk) 
    if request.method == 'POST':
        todo_list.delete()
        return redirect('home')
    else:
        return render(request, 'delete-list.html', {"todo_list": todo_list})

def deleted(request, pk):
    todo_list = TodoList.objects.get(pk = pk) 
    return render(request, "deleted.html", {"todo_list": todo_list})

