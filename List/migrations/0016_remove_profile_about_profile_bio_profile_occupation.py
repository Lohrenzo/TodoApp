# Generated by Django 4.1.4 on 2023-05-03 04:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("List", "0015_todolist_favourites"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="about",
        ),
        migrations.AddField(
            model_name="profile",
            name="bio",
            field=models.TextField(default="", max_length=2000),
        ),
        migrations.AddField(
            model_name="profile",
            name="occupation",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
