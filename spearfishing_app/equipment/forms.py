from django import forms

from spearfishing_app.equipment.models import Equipment


class EquipmentBaseForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = '__all__'


class EquipmentAddForm(EquipmentBaseForm):
    pass
