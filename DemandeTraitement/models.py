# DemandeTraitement/models.py
from django.db import models
from django.utils import timezone
from UserApp.models import RUser

class RendezVous(models.Model):
    
    date = models.DateTimeField()
    commentaire = models.TextField(blank=True, null=True)
    rdv_link = models.TextField(blank=True, null=True)
    def __str__(self):
        return f'Rendez-vous pour {self.date}'

class DemandeTraitement(models.Model):
    # Disease  = models.ForeignKey(DiseaseDetection, on_delete=models.CASCADE, related_name='demandes' , null = True)
    title_desease = models.CharField(max_length=150 , null = True)
    from_farmer = models.ForeignKey(RUser, on_delete=models.CASCADE, related_name='sent_demandes' , null=True)
    to_doc = models.ForeignKey(RUser, on_delete=models.CASCADE, related_name='received_demandes' , null=True)
    description = models.TextField()
    date_demande = models.DateTimeField(default=timezone.now)
    rendezv = models.ForeignKey(RendezVous , on_delete= models.CASCADE , null = True)

    status = models.CharField(
        max_length=20,
        choices=[
            ('on hold', 'En attente'),
            ('approved', 'Approuvé'),
            ('rejected', 'Rejeté')
        ],
        default='on hold'
    )

    def __str__(self):
        return f"Demande de traitement pour  {self.title_desease}"
