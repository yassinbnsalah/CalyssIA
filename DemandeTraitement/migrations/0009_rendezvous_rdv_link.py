# Generated by Django 4.1.13 on 2024-10-29 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DemandeTraitement', '0008_remove_rendezvous_demande_demandetraitement_rendezv'),
    ]

    operations = [
        migrations.AddField(
            model_name='rendezvous',
            name='rdv_link',
            field=models.TextField(blank=True, null=True),
        ),
    ]
