from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# from django.contrib.auth import get_user_model

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(null=True, blank=True, upload_to='profile')
    bio = models.TextField(max_length=2000, null=True, blank=True, default="")
    occupation = models.CharField(max_length=150, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)
    
    def save(self):
        super().save()

        pic = Image.open(self.profile_pic.path)

        if pic.height > 400 or pic.width > 400:
            output_size = (400, 400)
            pic.thumbnail(output_size)
            pic.save(self.profile_pic.path)


class TodoList(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    picture = models.ImageField(null=False, blank=False, upload_to='images')
    created = models.DateTimeField(auto_now_add=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    completion_date = models.DateField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name="likes", blank=True)
    favourites = models.ManyToManyField(User, related_name ='favourite', default = None, blank = None)

    def __str__(self):
        return self.title
    
    def total_likes(self):
        return self.likes.count()
    
    class Meta:
        verbose_name_plural='Todo Lists'
        ordering=('-created',)

class ListItem(models.Model):
    item_name = models.CharField(max_length=300)
    completed = models.ManyToManyField(User, related_name="completed", blank=True)
    item_list = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name="list_items")
    item_author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.item_list} --> {self.item_name}"

    def total_completed(self):
        return self.completed.count()


class Completed(models.Model):
    completer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="completer")
    item_completed = models.ForeignKey(ListItem, on_delete=models.CASCADE, related_name="item_completed")
    caption = models.TextField(blank=True, max_length=800)
    media_file = models.FileField(upload_to='completed_media/') 

class Comment(models.Model):
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name="todo_list")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField(max_length=900)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.todo_list) + " ==> " + str(self.body)


