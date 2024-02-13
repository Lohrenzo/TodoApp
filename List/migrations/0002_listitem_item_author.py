# Generated by Django 4.1.4 on 2023-04-29 19:42

import List.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("List", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="listitem",
            name="item_author",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]