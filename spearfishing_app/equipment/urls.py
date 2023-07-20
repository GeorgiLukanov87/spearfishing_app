from django.urls import path

from spearfishing_app.equipment.views import add_equipment, EquipmentEditView

urlpatterns = (
    path('add/', add_equipment, name='add-equipment'),
    path('edit/<int:pk>/', EquipmentEditView.as_view(), name='edit-equipment'),
)
