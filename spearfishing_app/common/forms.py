from django import forms

from spearfishing_app.common.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.TextInput(
                attrs={
                    'placeholder': 'Add comment...'
                },
            ),
        }


class SearchForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search...'
            }
        )
    )
