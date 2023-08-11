from django import forms

from spearfishing_app.equipment.models import Equipment


# equipment/forms.py
class EquipmentBaseForm(forms.ModelForm):
    class Meta:
        model = Equipment
        exclude = ('owner',)

        widgets = {
            'gun_image': forms.URLInput(
                attrs={
                    'placeholder': 'Link to gun image...'
                }
            ),

            'bands_image': forms.URLInput(
                attrs={
                    'placeholder': 'Link to bands image...'
                }
            ),

            'fins_image': forms.URLInput(
                attrs={
                    'placeholder': 'Link to fins image...'
                }
            ),

            'additional_info': forms.Textarea(
                attrs={
                    'placeholder': 'Add additional info here...'
                }
            ),
        }


class EquipmentAddForm(EquipmentBaseForm):
    pass
