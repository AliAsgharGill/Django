# Generated by Django 5.1.1 on 2024-09-12 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("firstapp", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Users",
            new_name="User",
        ),
    ]