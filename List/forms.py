from django import forms
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
        fields = ("item_name", "item_list")



