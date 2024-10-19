from django import forms
from .models import Treatment

class TreatmentForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = ['name', 'description', 'date_applied', 'success_rate', 'notes']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Treatment Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Treatment Description'}),
            'date_applied': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'success_rate': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Success Rate', 'step': '0.01'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Additional Notes'}),
        }
