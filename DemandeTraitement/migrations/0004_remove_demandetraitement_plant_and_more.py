# Generated by Django 4.1.13 on 2024-10-26 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PlantApp', '0003_alter_diseasedetection_confidence_score'),
        ('DemandeTraitement', '0003_demandetraitement_from_farmer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demandetraitement',
            name='plant',
        ),
        migrations.AddField(
            model_name='demandetraitement',
            name='Disease',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='demandes', to='PlantApp.diseasedetection'),
        ),
    ]
