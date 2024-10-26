from django.shortcuts import get_object_or_404, redirect, render
from .models import TypeMaladie
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import TypeMaladieForm

def home(request):
    return render(request, 'home.html')

def type_maladie_list(request):
    typemaladies = TypeMaladie.objects.all()  
    return render(request, 'type_maladie_list.html', {'typemaladies': typemaladies})

def create_type_maladie(request):
    if request.method == 'POST':
        form = TypeMaladieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('type_maladie_list') 
    else:
        form = TypeMaladieForm()
    
    return render(request, 'create_type_maladie.html', {'form': form})

def delete_type_maladie(request, pk):
    typemaladie = get_object_or_404(TypeMaladie, id=pk)
    typemaladie.delete()
    return redirect('type_maladie_list')

class TypeMaladieCreateView(CreateView):
    model = TypeMaladie
    form_class = TypeMaladieForm
    template_name = 'type_maladie_form.html'
    success_url = reverse_lazy('type_maladie_list')
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class TypeMaladieUpdateView(UpdateView):
    model = TypeMaladie
    form_class = TypeMaladieForm
    template_name = 'type_maladie_form.html'
    success_url = reverse_lazy('type_maladie_list')
 
    def get_queryset(self):
        return TypeMaladie.objects.filter(id=self.kwargs['pk'])

class TypeMaladieDeleteView(DeleteView):
    model = TypeMaladie
    template_name = 'type_maladie_confirm_delete.html'
    success_url = reverse_lazy('type_maladie_list')

    def get_queryset(self):
        return TypeMaladie.objects.filter(owner=self.request.user)
