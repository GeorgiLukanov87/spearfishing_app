from django import forms

from spearfishing_app.stories.models import Story


# stories/forms.py
class StoryBaseForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ('title', 'image_url', 'description',)

        labels = {
            'title': '',
            'image_url': '',
            'description': '',
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
                    'rows': 25,
                    'cols': 35,
                }
            ),

        }


class StoryCreateForm(StoryBaseForm):
    pass


class StoryEditForm(StoryBaseForm):
    class Meta:
        model = Story
        exclude = ('creator',)
