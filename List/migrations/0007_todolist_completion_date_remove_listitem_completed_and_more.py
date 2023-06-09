# Generated by Django 4.1.4 on 2023-05-01 13:13

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("List", "0006_delete_like"),
    ]

    operations = [
        migrations.AddField(
            model_name="todolist",
            name="completion_date",
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name="listitem",
            name="completed",
        ),
        migrations.AddField(
            model_name="listitem",
            name="completed",
            field=models.ManyToManyField(
                blank=True, related_name="completed", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
