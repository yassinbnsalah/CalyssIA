from django.db import models
from MethodeTraitementApp.models import MethodeTraitement
from UserApp.models import RUser 

class Treatment(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date_applied = models.DateTimeField( null=True)
    success_rate = models.FloatField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(RUser , on_delete=models.CASCADE , null = True)
    methodes_traitement = models.ManyToManyField(MethodeTraitement, blank=True, related_name="traitements")
    def __str__(self):
        return f'Treatment: {self.name}'
