# DemandeTraitement/views.py
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from PlantApp.models import DiseaseDetection
from .models import DemandeTraitement, RendezVous
from .forms import DemandeTraitementForm, RendezVousForm

from django.urls import reverse_lazy

from DemandeTraitement.calenderFCT import main

def createDemande(request, pk):
    disease = get_object_or_404(DiseaseDetection, id=pk)
    if request.method == 'POST':
        form = DemandeTraitementForm(request.POST)
        if form.is_valid():
            demande = form.save(commit=False)
            demande.status = "en_attente"
            
            demande.title_desease = disease.plant.name  +" is problem in "+ disease.detected_disease
            form.instance.from_farmer = request.user  
            demande.save()
            disease.demande = demande 
            disease.save()
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

from datetime import datetime, timedelta

def create_rendezvous(request, demande_id):
    # Get the associated DemandeTraitement object
    demande = get_object_or_404(DemandeTraitement, pk=demande_id)
    
    if request.method == 'POST':
        form = RendezVousForm(request.POST)
        if form.is_valid():
            rendezvous = form.save(commit=False)
            date_str =str(rendezvous.date)
            date_object = datetime.fromisoformat(date_str)
            formatted_date = date_object.isoformat()
            try:
                link = main(
                    "yacinbnsalh@gmail.com",
                    "wiem.benaraar@esprit.tn", 
                    formatted_date , 
                    demande.title_desease
                )
                rendezvous.rdv_link = link 
                current_user = request.user
                demande.from_farmer = current_user
                rendezvous.save()
                demande.rendezv = rendezvous
                demande.status = "approuve"
                demande.save()
                
                return redirect('demande_list')  # Redirect after successful creation

            except Exception as e:
                # Handle any exceptions, such as issues with the Google Calendar API
                print(f"An error occurred while creating the event: {e}")
                # You may want to add an error message to the context for user feedback
                context = {
                    'form': form,
                    'demande': demande,
                    'error': "An error occurred while creating the rendezvous. Please try again."
                }
                return render(request, 'demande_traitement/create_rendezvous.html', context)
    
    else:
        form = RendezVousForm()  # Create a new form instance if not a POST request

    # Prepare the context for rendering the template
    context = {
        'form': form,
        'demande': {
            'id': demande.id,
            'objet': demande.title_desease  # Replace with actual details if available
        }
    }

    return render(request, 'demande_traitement/create_rendezvous.html', context)
class RendezVousCreateView(CreateView):
    model = RendezVous
    form_class = RendezVousForm
    template_name = 'demande_traitement/create_rendezvous.html'
    success_url = reverse_lazy('demande_list')  # Redirige après succès

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Récupérer l'ID de la demande à partir de l'URL
        demande_id = self.kwargs.get('demande_id')
        # Simuler des détails de la demande sans utiliser un modèle
        context['demande'] = {
            'id': demande_id,
            'objet': "Objet fictif de la demande"  # Remplacez par les détails réels si disponibles
        }
        return context

    def form_valid(self, form):
        demande_id = self.kwargs.get('demande_id')
        if demande_id:
            form.instance.demande_id = demande_id  # Associer l'ID à votre instance de rendez-vous
            return super().form_valid(form)
        else:
            return redirect(self.success_url)
            
class DemandeTraitementDetailView(DetailView):
    model = DemandeTraitement
    template_name = 'demande_detail.html'  # Remplacez par votre modèle de template
    context_object_name = 'demande'
