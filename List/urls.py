from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('new_item/', views.new_item, name='new_item'),
    path('get_items/<int:pk>', views.get_items, name='get_items'),
    path('<int:pk>/edit-list/', views.edit_todolist, name='edit'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('deleted/<int:pk>', views.deleted, name='deleted'),
]

