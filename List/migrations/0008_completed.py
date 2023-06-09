# Generated by Django 4.1.4 on 2023-05-01 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("List", "0007_todolist_completion_date_remove_listitem_completed_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Completed",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("caption", models.TextField(blank=True, max_length=800)),
                ("media_file", models.FileField(upload_to="media_files/")),
                (
                    "item_completed",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="item_completed",
                        to="List.listitem",
                    ),
                ),
            ],
        ),
    ]
