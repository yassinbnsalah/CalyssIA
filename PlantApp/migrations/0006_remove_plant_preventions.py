# Generated by Django 5.1.2 on 2024-10-29 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PlantApp', '0005_plant_preventions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='preventions',
        ),
    ]