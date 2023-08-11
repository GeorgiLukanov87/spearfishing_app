from django import forms

from spearfishing_app.equipment.models import Equipment


# equipment/forms.py
class EquipmentBaseForm(forms.ModelForm):
    class Meta:
        model = Equipment
        exclude = ('owner',)

        labels = {
            'gun_image': '',
            'bands_image': '',
            'fins_image': '',
            'additional_info': '',
        }

        widgets = {
            'gun_image': forms.URLInput(
                attrs={
                    'placeholder': 'Link to your Gun image...'
                }
            ),

            'bands_image': forms.URLInput(
                attrs={
                    'placeholder': 'Link to your Bands image...'
                }
            ),

            'fins_image': forms.URLInput(
                attrs={
                    'placeholder': 'Link to your Fins image...'
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
