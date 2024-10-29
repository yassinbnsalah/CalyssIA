from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from UserApp.decorators import role_required
import os
import json  
import google.generativeai as genai
from django.utils import timezone  
from Maladie.models import Maladie
from .models import Treatment
from .forms import TreatmentForm

# Configure Google API
GOOGLE_API = 'AIzaSyANfuF0wGsR1M1wKZ2NvEaFjPPkZ-nWxGY'
genai.configure(api_key=GOOGLE_API)

# Function to generate treatment description
def ai_generate_treatment_description(maladie_name):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"Generate a detailed treatment description in 4 lines for the illness: {maladie_name}"
    response = model.generate_content(prompt)
    return response.text.strip()  

# AJAX view to generate treatment description
@csrf_exempt
def generate_treatment_description(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        maladie_name = data.get('maladie_name', '')
        description = ai_generate_treatment_description(maladie_name)
        return JsonResponse({'description': description})
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

# List of treatments view
@login_required 
@role_required("DOCTOR")
def treatment_list(request):
    treatments = Treatment.objects.all()  
    return render(request, 'treatment_list.html', {'treatments': treatments})

# Create treatment view
@login_required 
@role_required("DOCTOR")
def create_treatment(request, pk):
    maladie = get_object_or_404(Maladie, id=pk)
    
    if request.method == 'POST':
        form = TreatmentForm(request.POST)
        if form.is_valid():
            treatment = form.save(commit=False)
            treatment.maladie = maladie
            treatment.description = ai_generate_treatment_description(maladie.nom) 
            treatment.date_applied = timezone.now().date() 
            current_user = request.user
            treatment.owner = current_user
            treatment.save()
            maladie.traitements.add(treatment)
            return redirect('treatment_list')
    else:
        form = TreatmentForm()

    return render(request, 'treatment_form.html', {'form': form, 'maladie_name': maladie.nom})


@login_required 
@role_required("DOCTOR")
def treatment_detail(request, pk):
    treatment = get_object_or_404(Treatment, pk=pk)
    return render(request, 'treatment_detail.html', {'treatment': treatment})

class TreatmentCreateView(CreateView):
    model = Treatment
    form_class = TreatmentForm
    template_name = 'treatment_form.html'
    success_url = reverse_lazy('treatment_list')

class TreatmentUpdateView(UpdateView):
    model = Treatment
    form_class = TreatmentForm
    template_name = 'treatment_update_form.html' 
    success_url = reverse_lazy('treatment_list')

class TreatmentDeleteView(DeleteView):
    model = Treatment
    template_name = 'treatment_confirm_delete.html'
    success_url = reverse_lazy('treatment_list')
