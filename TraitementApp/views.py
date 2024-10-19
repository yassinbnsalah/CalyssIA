from django.shortcuts import render, redirect
from .models import Treatment
from .forms import TreatmentForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import  get_object_or_404

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

def treatment_detail(request, pk):
    treatment = get_object_or_404(Treatment, pk=pk)
    return render(request, 'treatment_detail.html', {'treatment': treatment})

class TreatmentDeleteView(DeleteView):
    model = Treatment
    success_url = reverse_lazy('treatment_list')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)