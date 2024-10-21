from django.urls import path
from .views import (
    prevention_list,
    create_prevention,
    PreventionCreateView,
    PreventionUpdateView,
    PreventionDeleteView,
    prevention_detail
)

urlpatterns = [
    path('preventions/', prevention_list, name='prevention_list'),
    path('preventions/create/', create_prevention, name='prevention-create'),
    path('preventions/<int:pk>/', prevention_detail, name='prevention_detail'),
    path('preventions/<int:pk>/edit/', PreventionUpdateView.as_view(), name='prevention_update'),
    path('preventions/<int:pk>/delete/', PreventionDeleteView.as_view(), name='prevention_delete'),
    
]
