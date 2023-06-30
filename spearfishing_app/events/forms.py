from django import forms

from spearfishing_app.events.models import Event


class EventBaseForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        labels = {
            'image_url': 'Image URL',
            'start_date': 'Start Date'
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


class EventDeleteForm(EventBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __disable_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True
            field.required = False
