from django import forms

from spearfishing_app.locations.models import Search


# locations/forms.py
class SearchLocationForm(forms.ModelForm):
    address = forms.CharField(label='')

    class Meta:
        model = Search
        fields = ['address', ]
