# Generated by Django 4.2.4 on 2023-08-24 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0020_aboutus_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='first_name',
            field=models.CharField(default='Joe Doe', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='last_name',
            field=models.CharField(default='JoeDoe', max_length=50),
            preserve_default=False,
        ),
    ]
