from .models import TodoList, ListItem
from .forms import *

def lists(request):
    lists = TodoList.objects.all()
    return {'lists': lists}

# def edit_todolist(request, pk):
#     todolist = TodoList.objects.get(pk = pk)
#     form = TodoListForm(instance=todolist)
#     return {'todolist': todolist, 'form': form}

# def list_items(request, pk = TodoList.pk):
#         todo_list = TodoList.objects.get(pk = pk) 
#         # list_items = todo_list.listitem_set.all() # 1st Option (Reverse Relationship). Write the ListItem model in small letter followed by "_set". 
#         list_items = todo_list.list_items.all() # 2nd Option (Reverse Relationship).
#         context = {
#             "todo_list": todo_list,
#             "list_items": list_items,
#             # 'pk': pk
#         }
#         return context

# def list_items(request, pk = None):
#     if pk is not None:
#         todo_list = TodoList.objects.get(pk=pk)
#         list_items = todo_list.list_items.all()
#     else:
#         todo_list = None
#         list_items = []
#     context = {
#         "todo_list": todo_list,
#         "list_items": list_items,
#     }
#     return context
