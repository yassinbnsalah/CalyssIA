from django.shortcuts import render, redirect
from .models import Plant
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .forms import PlantForm
def home(request):
    return render(request, 'home.html')


def plant_list(request):
    plants = Plant.objects.all()  
    return render(request, 'plant_list.html', {'plants': plants})


def create_plant(request):
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('plant_list') 
    else:
        form = PlantForm()
    
    return render(request, 'create_plant.html', {'form': form})


class PlantCreateView(CreateView):
    model = Plant
    fields = ['name', 'scientific_name', 'description', 'image']
    template_name = 'plant_form.html'
    success_url = reverse_lazy('plant_list')    
    def form_valid(self, form):
        form.instance.owner = self.request.user  
        return super().form_valid(form)


class PlantUpdateView(UpdateView):
    model = Plant
    fields = ['name', 'scientific_name', 'description', 'image']
    template_name = 'plant_form.html'
    success_url = reverse_lazy('plant_list')
    def get_queryset(self):
        return Plant.objects.filter(id=self.kwargs['pk'])



class PlantDeleteView(DeleteView):
    model = Plant
    template_name = 'plant_confirm_delete.html'
    success_url = reverse_lazy('plant_list')

    def get_queryset(self):
        return Plant.objects.filter(owner=self.request.user)