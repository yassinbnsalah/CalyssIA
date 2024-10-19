from django.urls import path
from .views import TreatmentListView, TreatmentDetailView, TreatmentCreateView, TreatmentUpdateView, TreatmentDeleteView

urlpatterns = [
    path('treatments/', TreatmentListView.as_view(), name='treatment_list'),
    path('treatments/<int:pk>/', TreatmentDetailView.as_view(), name='treatment_detail'),
    path('treatments/create/', TreatmentCreateView.as_view(), name='treatment_create'),
    path('treatments/<int:pk>/update/', TreatmentUpdateView.as_view(), name='treatment_update'),
    path('treatments/<int:pk>/delete/', TreatmentDeleteView.as_view(), name='treatment_delete'),
]
