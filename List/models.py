from django.db import models

# Create your models here.
class TodoList(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    picture = models.ImageField(null=False, blank=False, upload_to='images')
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class ListItem(models.Model):
    item_name = models.CharField(max_length=300)
    completed = models.BooleanField(default=False)
    item_list = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name="list_items")

    def __str__(self):
        return f"{self.item_list} --> {self.item_name}"

