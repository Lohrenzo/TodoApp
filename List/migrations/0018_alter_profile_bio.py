# Generated by Django 4.1.4 on 2023-05-06 12:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("List", "0017_alter_profile_profile_pic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="bio",
            field=models.TextField(blank=True, default="", max_length=2000, null=True),
        ),
    ]
