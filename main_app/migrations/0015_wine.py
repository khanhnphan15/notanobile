# Generated by Django 4.2.4 on 2023-08-22 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_alter_reservation_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
