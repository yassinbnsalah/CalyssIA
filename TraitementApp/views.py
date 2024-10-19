from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Treatment
from .forms import TreatmentForm
from django.shortcuts import render, redirect


# List all treatments (Read)
class TreatmentListView(ListView):
    model = Treatment
    template_name = 'treatment_list.html'
    context_object_name = 'treatments'

# View a specific treatment (Read)
class TreatmentDetailView(DetailView):
    model = Treatment
    template_name = 'treatment_detail.html'
    context_object_name = 'treatment'


def create_treatment(request):
    if request.method == 'POST':
        form = TreatmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('treatment_list') 
    else:
        form = TreatmentForm()
    
    return render(request, 'treatment_form.html', {'form': form})

# Create a new treatment (Create)
class TreatmentCreateView(CreateView):
    model = Treatment
    form_class = TreatmentForm
    template_name = 'treatment_form.html'
    success_url = reverse_lazy('treatment_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user  
        return super().form_valid(form)

# Update an existing treatment (Update)
class TreatmentUpdateView(UpdateView):
    model = Treatment
    form_class = TreatmentForm
    template_name = 'treatment_form.html'
    success_url = reverse_lazy('treatment_list')

# Delete a treatment (Delete)
class TreatmentDeleteView(DeleteView):
    model = Treatment
    template_name = 'treatment_confirm_delete.html'
    success_url = reverse_lazy('treatment_list')
