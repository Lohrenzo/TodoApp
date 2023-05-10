from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
# from django.forms import ModelForm
from .models import *

class TodoListForm(forms.ModelForm):

    class Meta:
        model = TodoList
        fields = ("title", "description")

        widgets = {
            'title': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    # 'placeholder': 'Title',
                }
            ),
            'description': forms.Textarea(
                attrs = {
                    'class': 'form-control',
                }
            ),
            # 'picture': forms.FileInput(
            #     attrs = {
            #         'class': 'form-control'
            #     }
            # )
        }


class ListItemForm(forms.ModelForm):

    class Meta:
        model = ListItem
        # fields = "__all__"
        fields = ("item_name",)

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ("body",)

        widgets = {
            'body': forms.Textarea(
                attrs = {
                    'class': 'form-control',
                    "placeholder": "Write a comment"
                }
            ),
        }

# class LikeForm(forms.ModelForm):

#     class Meta:
#         model = Like
#         fields = "__all__"

class ProfilePageForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'occupation', 'facebook_url', 'twitter_url', 'instagram_url')
        widgets = {
            'bio': forms.Textarea(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'profile_pic': forms.FileInput(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'occupation': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'facebook_url': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'twitter_url': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'instagram_url': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                }
            ),
        }


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs= {'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs= {'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs= {'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs= {'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')


