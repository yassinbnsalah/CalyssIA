# Generated by Django 4.1.13 on 2024-10-26 10:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0002_alter_ruser_options_alter_ruser_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ruser',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]