from django.shortcuts import render, redirect, get_object_or_404
from .models import Prevention
from .forms import PreventionForm
from FeedbacksApp.forms import FeedbackForm  # Adjusted import for FeedbackForm
from FeedbacksApp.models import Feedback  # Adjusted import for FeedbackForm
from PlantApp.models import Plant
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from UserApp.decorators import role_required
from django.shortcuts import render, redirect, get_object_or_404
import openai  
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.decorators import login_required
from UserApp.decorators import role_required
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Prevention
from .forms import PreventionForm
from FeedbacksApp.forms import FeedbackForm
from FeedbacksApp.models import Feedback
from PlantApp.models import Plant
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from UserApp.decorators import role_required
from openai import OpenAI 
from django.http import JsonResponse
from django.views import View
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# Set the OpenAI API Key directly
#OPENAI_API_KEY = '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'
#openai.api_key = OPENAI_API_KEY

client = OpenAI(api_key="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")

@login_required
def chat_view(request):
    return render(request, 'Templates/chat.html')

@method_decorator(csrf_exempt, name='dispatch')
class ChatWithPreventionAI(View):
    def post(self, request):
        try:
            # Parse JSON data from the request body
            data = json.loads(request.body)
            user_input = data.get('query')

            if not user_input:
                return JsonResponse({"error": "No query provided"}, status=400)

            # Use the new client instance to call Chat Completion
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}]
            )
            answer = response.choices[0].message.content
            return JsonResponse({"response": answer}, status=200)

        except json.JSONDecodeError:
            # Handle cases where JSON parsing fails
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

        except Exception as e:
            # Catch-all for any other exceptions
            return JsonResponse({"error": str(e)}, status=500)

@login_required 
@role_required("DOCTOR")
def prevention_list(request):
    preventions = Prevention.objects.all()  
    return render(request, 'prevention_list.html', {'preventions': preventions})
@login_required 
@role_required("DOCTOR")
def create_prevention(request,pk):
    if request.method == 'POST':
        plant = get_object_or_404(Plant, id=pk)
        form = PreventionForm(request.POST)
        if form.is_valid():
            form.save()
            prevention = form.save()
            plant.preventions.add(prevention)
            return redirect('prevention_list') 
    else:
        form = PreventionForm()
    return render(request, 'prevention_form.html', {'form': form})

    

# Class-based view for creating a new Prevention record
class PreventionCreateView(CreateView):
    model = Prevention
    form_class = PreventionForm
    template_name = 'prevention_form.html'
    success_url = reverse_lazy('prevention_list')  # Redirect to the prevention list after saving

# Class-based view for updating a Prevention record
class PreventionUpdateView(UpdateView):
    model = Prevention
    form_class = PreventionForm
    template_name = 'prevention_update_form.html'  # Separate template for updating Prevention
    success_url = reverse_lazy('prevention_list')

# Class-based view for deleting a Prevention record
class PreventionDeleteView(DeleteView):
    model = Prevention
    template_name = 'prevention_confirm_delete.html'
    success_url = reverse_lazy('prevention_list')

# Function-based view for showing the details of a Prevention record
@login_required 
@role_required("DOCTOR")
def prevention_detail(request, pk):
    prevention = get_object_or_404(Prevention, pk=pk)
    feedbacks = Feedback.objects.filter(prevention=prevention)  
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.prevention = prevention 
            feedback.save()
            return redirect('prevention_detail', pk=prevention.pk)  
    else:
        form = FeedbackForm() 

    return render(request, 'prevention_detail.html', {
        'prevention': prevention,
        'feedbacks': feedbacks,
        'form': form,  
    })









# Class-based view for creating a new Prevention record
class PreventionCreateView(CreateView):
    model = Prevention
    form_class = PreventionForm
    template_name = 'prevention_form.html'
    success_url = reverse_lazy('prevention_list')  # Redirect to the prevention list after saving

# Class-based view for updating a Prevention record
class PreventionUpdateView(UpdateView):
    model = Prevention
    form_class = PreventionForm
    template_name = 'prevention_update_form.html'  # Separate template for updating Prevention
    success_url = reverse_lazy('prevention_list')

# Class-based view for deleting a Prevention record
class PreventionDeleteView(DeleteView):
    model = Prevention
    template_name = 'prevention_confirm_delete.html'
    success_url = reverse_lazy('prevention_list')

# Function-based view for showing the details of a Prevention record
@login_required 
@role_required("DOCTOR")
def prevention_detail(request, pk):
    prevention = get_object_or_404(Prevention, pk=pk)
    feedbacks = Feedback.objects.filter(prevention=prevention)  
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.prevention = prevention 
            feedback.save()
            return redirect('prevention_detail', pk=prevention.pk)  
    else:
        form = FeedbackForm() 

    return render(request, 'prevention_detail.html', {
        'prevention': prevention,
        'feedbacks': feedbacks,
        'form': form,  
    })
