# Generated by Django 4.2.4 on 2023-08-22 05:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_app", "0013_alter_reservation_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reservation",
            name="phone",
            field=models.CharField(max_length=50),
        ),
    ]
