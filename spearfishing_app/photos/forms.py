import os

from django import forms

from spearfishing_app.common.models import Like, Comment
from spearfishing_app.photos.disable_form_mixin import DisabledFormMixin
from spearfishing_app.photos.models import Photo


# photos/forms.py
class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        # fields = '__all__'
        exclude = ['user', ]

        widgets = {
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Add description...'
                }
            ),
            'location': forms.TextInput(
                attrs={
                    'placeholder': 'Add location...'
                }
            ),
        }


class PhotoCreateForm(PhotoBaseForm):
    class Meta:
        model = Photo
        fields = ('photo', 'description', 'location',)

        labels = {
            'photo': '',
            'description': '',
            'location': '',
        }

        widgets = {
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Add description...',
                    'rows': 15,
                    'cols': 35,
                }
            ),
            'location': forms.TextInput(
                attrs={
                    'placeholder': 'Add location...'
                }
            ),
        }


class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['photo', 'user']


class PhotoDeleteForm(DisabledFormMixin, PhotoEditForm):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        photo = Photo.objects.filter(pk=self.instance.id).get()
        if commit:
            Like.objects.filter(to_photo_id=self.instance.id).delete()  # one-to-many
            Comment.objects.filter(to_photo_id=self.instance.id).delete()  # one-to-many
            if photo.photo:
                # Get the local filesystem path to the photo
                photo_path = photo.photo.path

                # Check if the file exists before attempting to delete
                if os.path.exists(photo_path):
                    # Delete the file from the save_folder
                    os.remove(photo_path)

            self.instance.delete()

        return self.instance
