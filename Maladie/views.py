
from django.shortcuts import get_object_or_404, redirect,render
from .models import Maladie
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import MaladieForm
# views.py
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
import google.generativeai as genai
import json

# Set up the Google API key
GOOGLE_API = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API)

def ai_generate_description(title):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"generate a detailed description in 4 lines for: {title}"
    response = model.generate_content(prompt)
    
    # Assuming response has a 'content' attribute that holds the generated text
    return response.get('content', '')

@csrf_exempt
def generate_description(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title', '')
        description = ai_generate_description(title)
        return JsonResponse({'description': description})
    
    return JsonResponse({'error': 'Invalid Request'}, status=400)


def home(request):
    return render(request, 'home.html')

 
def maladie_list(request):
    maladies = Maladie.objects.all()  
    return render(request, 'maladie_list.html', {'maladies': maladies})

def maladie_list_farmer(request):
    maladies = Maladie.objects.all()  
    return render(request, 'maladie_list_farmer.html', {'maladies': maladies})

def create_maladie(request):
    if request.method == 'POST':
        form = MaladieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('maladie_list') 
    else:
        form = MaladieForm()
    
    return render(request, 'create_maladie.html', {'form': form})


def delete_maladie(request, pk):
        maladie = get_object_or_404(Maladie, id=pk)  # Retrieve the object
        maladie.delete()  # Delete the object
        return redirect('maladie_list')  # Redirect after deletion


class MaladieCreateView(CreateView):
    model = Maladie
    fields = ['nom', 'description', 'image', 'causes', 'symptomes']
    template_name = 'maladie_form.html'
    success_url = reverse_lazy('maladie_list')    
    def form_valid(self, form):
        form.instance.owner = self.request.user  
        return super().form_valid(form)


class MaladieUpdateView(UpdateView):
    model = Maladie
    fields = ['nom', 'description', 'image', 'causes', 'symptomes']
    template_name = 'maladie_form.html'
    success_url = reverse_lazy('maladie_list')
    def get_queryset(self):
        return Maladie.objects.filter(id=self.kwargs['pk'])


class MaladieDeleteView(DeleteView):
    model = Maladie
    template_name = 'maladie_comfirm_delete.html'
    success_url = reverse_lazy('maladie_list')

    def get_queryset(self):
        return Maladie.objects.filter(owner=self.request.user)
