# Generated by Django 4.1.13 on 2024-10-20 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TraitementApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='date_applied',
            field=models.DateTimeField(null=True),
        ),
    ]
