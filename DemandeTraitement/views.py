# DemandeTraitement/views.py
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from PlantApp.models import DiseaseDetection
from .models import DemandeTraitement, RendezVous
from .forms import DemandeTraitementForm, RendezVousForm

from django.urls import reverse_lazy



def createDemande(request, pk):
    disease = get_object_or_404(DiseaseDetection, id=pk)
    if request.method == 'POST':
        form = DemandeTraitementForm(request.POST)
        if form.is_valid():
            demande = form.save(commit=False)
            demande.disease = disease
            demande.save()
            return redirect('PlantApp:details_plant', pk=disease.plant.id)
    else:
        form = DemandeTraitementForm()
    return render(request, 'demande_traitement/create.html', {'form': form, 'disease': disease})

class DemandeTraitementCreateView(CreateView):
    model = DemandeTraitement
    form_class = DemandeTraitementForm
    template_name = 'demande_traitement/create.html'  # Vérifie que le chemin est correct
    success_url = reverse_lazy('demande_list')  # Assure-toi que cette URL est bien définie

class DemandeTraitementListView(ListView):
    model = DemandeTraitement
    template_name = 'demande_traitement/list.html' 
    context_object_name = 'demandes' 
def DemandeTraitementUpdateView(request, pk):
    demande = get_object_or_404(DemandeTraitement, pk=pk)
    if request.method == 'POST':
        form = DemandeTraitementForm(request.POST, instance=demande)
        if form.is_valid():
            form.save()
            return redirect('demande_list')  # Rediriger vers la liste après mise à jour
    else:
        form = DemandeTraitementForm(instance=demande)
    return render(request, 'demande_traitement/create.html', {'form': form})

# Vue pour supprimer une demande de traitement
def DemandeTraitementDeleteView(request, pk):
    demande = get_object_or_404(DemandeTraitement, pk=pk)
    if request.method == 'POST':
        demande.delete()
        return redirect('demande_list')  # Rediriger vers la liste après suppression
    return render(request, 'demande_traitement/confirm_delete.html', {'demande': demande})


class RendezVousCreateView(CreateView):
    model = RendezVous
    form_class = RendezVousForm
    template_name = 'demande_traitement/create_rendezvous.html'
    success_url = reverse_lazy('demande_list')


class DemandeTraitementDetailView(DetailView):
    model = DemandeTraitement
    template_name = 'demande_detail.html'  # Remplacez par votre modèle de template
    context_object_name = 'demande'
