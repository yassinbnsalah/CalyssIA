# Generated by Django 4.1.13 on 2024-10-27 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DemandeTraitement', '0005_merge_20241027_1015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demandetraitement',
            name='Disease',
        ),
    ]
