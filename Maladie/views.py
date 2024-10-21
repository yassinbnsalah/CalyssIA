
from django.shortcuts import get_object_or_404, redirect,render
from .models import Maladie
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import MaladieForm

def home(request):
    return render(request, 'home.html')

 
def maladie_list(request):
    maladies = Maladie.objects.all()  
    return render(request, 'maladie_list.html', {'maladies': maladies})


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
