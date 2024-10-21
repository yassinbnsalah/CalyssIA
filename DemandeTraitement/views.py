# DemandeTraitement/views.py
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView
from .models import DemandeTraitement
from .forms import DemandeTraitementForm
from django.urls import reverse_lazy
class DemandeTraitementCreateView(CreateView):
    model = DemandeTraitement
    form_class = DemandeTraitementForm
    template_name = 'demande_traitement/create.html'  # Vérifie que le chemin est correct
    success_url = reverse_lazy('demande_list')  # Assure-toi que cette URL est bien définie

class DemandeTraitementListView(ListView):
    model = DemandeTraitement
    template_name = 'demande_traitement/list.html'  # Modifie en fonction de ton template
    context_object_name = 'demandes'  # Le nom de la variable de contexte pour la template
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