# Generated by Django 4.2.4 on 2023-08-20 13:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main_app", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Meals",
            new_name="Meal",
        ),
    ]
