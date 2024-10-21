# Generated by Django 5.1.2 on 2024-10-19 20:59

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('PlantApp', '0002_alter_plant_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='DemandeTraitement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('date_demande', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('en_attente', 'En attente'), ('approuve', 'Approuvé'), ('rejeté', 'Rejeté')], max_length=20)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='demandes', to='PlantApp.plant')),
            ],
        ),
    ]
