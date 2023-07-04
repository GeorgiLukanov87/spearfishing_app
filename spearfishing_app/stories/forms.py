from django import forms

from spearfishing_app.stories.models import Story


class StoryBaseForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = "__all__"

        labels = {
            'title': '',
            'image_url': '',
        }

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Add Title...'
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Link to photo...'
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Tell your story...',
                    'rows': 30,
                    'cols': 40,
                }
            ),
        }


class StoryCreateForm(StoryBaseForm):
    pass


class StoryEditForm(StoryBaseForm):
    pass
