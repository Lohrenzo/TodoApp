from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(TodoList)
admin.site.register(ListItem)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(Completed)
