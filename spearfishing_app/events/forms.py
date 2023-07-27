from django import forms

from spearfishing_app.events.models import Event
from spearfishing_app.photos.disable_form_mixin import DisabledFormMixin


# events/forms.py
class EventBaseForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ('start_date',)
        # fields = '__all__'
        labels = {
            'image_url': 'Image URL',
            'start_date': 'Start Date',
            'competitors': 'Add Competitors',
        }

        widgets = {
            'start_date': forms.DateTimeInput(
                attrs={
                    'placeholder': 'Add Start Date...'
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Link to image'
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Tournament name...'
                }
            ),
            'location': forms.TextInput(
                attrs={
                    'placeholder': 'Add Location...'
                }
            ),
        }


class EventCreateForm(EventBaseForm):
    pass


class EventEditForm(EventBaseForm):
    pass


class EventDeleteForm(DisabledFormMixin, EventBaseForm):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
