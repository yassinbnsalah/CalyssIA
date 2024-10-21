from django.urls import path
from .views import delete_maladie, maladie_list, home, create_maladie
from .views import MaladieCreateView, MaladieUpdateView, MaladieDeleteView

urlpatterns = [
    path('test/', home, name='home'),
    path('maladies/', maladie_list, name='maladie_list'),
    path('maladies/create/', create_maladie, name='maladie-create'),
    path('maladies/<int:pk>/update/', MaladieUpdateView.as_view(), name='maladie-update'),
    path('maladies/<int:pk>/delete/', delete_maladie, name='delete_maladie'),
]
