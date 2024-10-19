from django.shortcuts import render, redirect
from .models import Treatment
from .forms import TreatmentForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def treatment_list(request):
    treatments = Treatment.objects.all()  
    return render(request, 'treatment_list.html', {'treatments': treatments})

def create_treatment(request):
    if request.method == 'POST':
        form = TreatmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('treatment_list') 
    else:
        form = TreatmentForm()
    
    return render(request, 'treatment_form.html', {'form': form})

class TreatmentCreateView(CreateView):
    model = Treatment
    form_class = TreatmentForm
    template_name = 'treatment_form.html'
    success_url = reverse_lazy('treatment_list')

class TreatmentUpdateView(UpdateView):
    model = Treatment
    form_class = TreatmentForm
    template_name = 'treatment_form.html'
    success_url = reverse_lazy('treatment_list')

class TreatmentDeleteView(DeleteView):
    model = Treatment
    template_name = 'treatment_confirm_delete.html'
    success_url = reverse_lazy('treatment_list')
