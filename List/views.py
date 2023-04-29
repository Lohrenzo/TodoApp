from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
# from django.db.models import F
from .models import TodoList, ListItem
from django.contrib import messages
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
# from django.template import RequestContext


# Create your views here.
@login_required
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

@login_required
def search_list(request):
    if request.method == "POST":
        searched = request.POST['searched']
        lists = TodoList.objects.filter(title__contains = searched)
        return render(request, 'search-list.html', {'searched': searched, 'lists': lists})
    else:
        return render(request, 'search-list.html', {})


@login_required
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

@login_required
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

@login_required
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

@login_required
def delete(request, pk):
    todo_list = TodoList.objects.get(pk = pk) 
    if request.method == 'POST':
        todo_list.delete()
        return redirect('home')
    else:
        return render(request, 'delete-list.html', {"todo_list": todo_list})

@login_required
def deleted(request, pk):
    todo_list = TodoList.objects.get(pk = pk) 
    return render(request, "deleted.html", {"todo_list": todo_list})

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                return redirect('register')
            else:
                new_user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password)
                new_user.save()
                return redirect('home')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'Register.html')

def user_login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password =password)
        if user is not None:
            login(request, user)
            # return redirect('home')
            return redirect(request.GET.get('next', reverse('home')))
        else:
            messages.info(request,'Invalid Login Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect('home')
