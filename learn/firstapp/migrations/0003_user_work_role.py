# Generated by Django 5.1.1 on 2024-09-12 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("firstapp", "0002_rename_users_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="work_role",
            field=models.TextField(default=""),
        ),
    ]
