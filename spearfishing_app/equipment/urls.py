from django.urls import path

from spearfishing_app.equipment.views import add_equipment

urlpatterns = (
    path('add/', add_equipment, name='add-equipment'),
)
