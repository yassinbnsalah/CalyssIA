# DemandeTraitement/forms.py
from django import forms
from .models import DemandeTraitement

class DemandeTraitementForm(forms.ModelForm):
    class Meta:
        model = DemandeTraitement
        fields = ['plant', 'description', 'status']
        
    def __init__(self, *args, **kwargs):
        super(DemandeTraitementForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = True  # Rendre le champ description obligatoire
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Décrivez votre demande ici'})  # Ajouter des classes et un placeholder
