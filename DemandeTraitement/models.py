# DemandeTraitement/models.py
from django.db import models
from django.utils import timezone
from PlantApp.models import Plant


class DemandeTraitement(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='demandes')
    description = models.TextField()
    date_demande = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=[
        ('en_attente', 'En attente'),
        ('approuve', 'Approuvé'),
        ('rejeté', 'Rejeté')
    ])

    def __str__(self):
        return f"Demande de traitement pour {self.plant.name} - {self.status}"