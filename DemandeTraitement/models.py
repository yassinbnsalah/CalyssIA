# DemandeTraitement/models.py
from django.db import models
from django.utils import timezone
from PlantApp.models import Plant
from UserApp.models import RUser



class DemandeTraitement(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='demandes')
    from_farmer = models.ForeignKey(RUser, on_delete=models.CASCADE, related_name='sent_demandes' , null=True)
    to_doc = models.ForeignKey(RUser, on_delete=models.CASCADE, related_name='received_demandes' , null=True)
    description = models.TextField()
    date_demande = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=20,
        choices=[
            ('en_attente', 'En attente'),
            ('approuve', 'Approuvé'),
            ('rejeté', 'Rejeté')
        ],
        default='en_attente'
    )

    def __str__(self):
        return f"Demande de traitement pour {self.plant.name} - Status: {self.get_status_display()}"
class RendezVous(models.Model):
    demande = models.ForeignKey(DemandeTraitement, on_delete=models.CASCADE, related_name='rendez_vous')
    date = models.DateTimeField()
    commentaire = models.TextField(blank=True)

    def __str__(self):
        return f"Rendez-vous pour {self.demande.plant.name} le {self.date}"