# Generated by Django 4.2.4 on 2023-08-22 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("main_app", "0010_category_alter_aboutus_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="meal",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="main_app.category",
            ),
        ),
    ]
