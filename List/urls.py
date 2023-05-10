from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='home'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    # path('get_items/<int:pk>', views.get_items, name='get_items'),
    path('<int:pk>/edit-list/', views.edit_todolist, name='edit'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('delete-item/<int:list_pk>/<int:item_pk>/', views.delete_list_item, name='delete_list_item'),
    path('completed-item/<int:list_pk>/<int:item_pk>/', views.completed_list_item, name='completed_list_item'),
    path('<int:pk>/like/', views.like, name='like'),
    path('comment/<int:pk>/', views.comment, name='comment'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('search-list/', views.search_list, name="search_list"),
    path('fav/<int:id>/', views.add_favourite, name='add-favourite'),
    path('favourites/', views.favourite_list, name='favourite-list'),
    path('<int:id>/profile/', views.user_profile, name='user-profile'),
    path('edit/<int:id>/profile/', views.edit_profile, name='edit-profile'),
    
    # Password Reset
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

