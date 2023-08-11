from django import forms

from spearfishing_app.equipment.models import Equipment


# equipment/forms.py
class EquipmentBaseForm(forms.ModelForm):
    class Meta:
        model = Equipment
        exclude = ('owner',)


class EquipmentAddForm(EquipmentBaseForm):
    pass
