from django import forms

from spearfishing_app.common.models import Like, Comment
from spearfishing_app.photos.models import Photo


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'


class PhotoCreateForm(PhotoBaseForm):
    pass


class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['photo']


class PhotoDeleteForm(PhotoEditForm):
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if commit:
            # self.instance.tagged_users.clear()  # many-to-many
            # Photo.objects.all().first().tagged_pets.clear()

            Like.objects.filter(to_photo_id=self.instance.id).delete()  # one-to-many
            Comment.objects.filter(to_photo_id=self.instance.id).delete()  # one-to-many

            self.instance.delete()

        return self.instance
