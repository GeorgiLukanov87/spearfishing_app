from django import forms

from spearfishing_app.common.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

        labels = {
            'text': ''
        }

        widgets = {
            'text': forms.TextInput(
                attrs={
                    'placeholder': 'Add comment...'
                },
            ),
        }


class SearchForm(forms.Form):
    search_photo = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search...'
            }
        )
    )
