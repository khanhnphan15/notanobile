# Generated by Django 4.2.4 on 2023-08-23 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_wine'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='wines',
            field=models.ManyToManyField(to='main_app.wine'),
        ),
    ]
