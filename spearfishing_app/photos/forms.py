from django import forms

from spearfishing_app.common.models import Like, Comment
from spearfishing_app.photos.disable_form_mixin import DisabledFormMixin
from spearfishing_app.photos.models import Photo


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'
        labels = {
            'user': 'Owner'
        }

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
    pass


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
        if commit:
            Like.objects.filter(to_photo_id=self.instance.id).delete()  # one-to-many
            Comment.objects.filter(to_photo_id=self.instance.id).delete()  # one-to-many

            self.instance.delete()

        return self.instance
