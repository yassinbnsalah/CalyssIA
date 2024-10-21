# DemandeTraitement/urls.py
from django.urls import path
from .views import DemandeTraitementCreateView, DemandeTraitementListView, DemandeTraitementUpdateView, DemandeTraitementDeleteView

urlpatterns = [
    path('create/', DemandeTraitementCreateView.as_view(), name='demande_create'),  # Vue pour créer une demande
    path('', DemandeTraitementListView.as_view(), name='demande_list'),  # Vue pour lister les demandes
    path('update/<int:pk>/', DemandeTraitementUpdateView, name='demande_update'),  # Route pour la mise à jour
    path('delete/<int:pk>/', DemandeTraitementDeleteView, name='demande_delete'),
]
