from django import forms
from .models import Maladie

class MaladieForm(forms.ModelForm):
    class Meta:
        model = Maladie
        fields = ['nom', 'description', 'image', 'is_contagious'] 
         
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de la maladie'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description de la maladie'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'is_contagious': forms.CheckboxInput(attrs={'class': 'form-check-input'}),  
        }
