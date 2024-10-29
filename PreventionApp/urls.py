from django.urls import path
from .views import (
    prevention_list,
    create_prevention,
    PreventionCreateView,
    PreventionUpdateView,
    PreventionDeleteView,
    ChatWithPreventionAI,
    chat_view,
    prevention_detail)
from FeedbacksApp.views import feedback_list  
 

urlpatterns = [
    path('preventions/', prevention_list, name='prevention_list'),
    path('preventions/create/<int:pk>/', create_prevention, name='prevention-create'),
    path('preventions/<int:pk>/', prevention_detail, name='prevention_detail'),
    path('preventions/<int:pk>/edit/', PreventionUpdateView.as_view(), name='prevention_update'),
    path('preventions/<int:pk>/delete/', PreventionDeleteView.as_view(), name='prevention_delete'),
    path('preventions/<int:prevention_id>/feedbacks/', feedback_list, name='feedback_list'), 
    path('api/preventions/chat/', ChatWithPreventionAI.as_view(), name='chat_with_prevention_ai'),
    path('preventions/chat/', chat_view, name='chat_view'),  # URL for rendering chat.html
]
