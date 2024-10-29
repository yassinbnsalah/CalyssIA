from django.db import models
from TypeMaladie.models import TypeMaladie  
from TraitementApp.models import Treatment
from UserApp.models import RUser  

class Maladie(models.Model):
    nom = models.CharField(max_length=200, unique=True, verbose_name="Nom de la maladie")
    description = models.TextField(verbose_name="Description de la maladie")
    image = models.ImageField(upload_to='maladies/', verbose_name="Image de la maladie", null=True, blank=True)
    causes = models.TextField(verbose_name="Causes de la maladie", blank=True)
    symptomes = models.TextField(verbose_name="Symptomes observables", blank=True)
    date_publication = models.DateTimeField(auto_now_add=True, verbose_name="Date de publication")
    types = models.ManyToManyField(TypeMaladie, related_name='maladies', verbose_name="Types de maladies")
    add_by = models.ForeignKey(RUser , null = True , on_delete= models.CASCADE )
    traitements = models.ManyToManyField(Treatment, related_name="maladies", verbose_name="Traitements")

    class Meta:
        verbose_name = "Maladie"
        verbose_name_plural = "Maladies"
        ordering = ['-date_publication']

    def __str__(self):
        return self.nom
