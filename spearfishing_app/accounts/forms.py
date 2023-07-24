from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


# accounts/forms.py
class UserEditForm(auth_forms.UserChangeForm):
    class Meta:
        model = UserModel
        fields = ('first_name',)
        field_classes = {'username': auth_forms.UsernameField}


class UserCreateForm(auth_forms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter Password...'
        self.fields['password2'].widget.attrs['placeholder'] = 'Repeat Password...'

    class Meta:
        model = UserModel
        fields = ('username', 'email', 'profile_image_url',)
        field_classes = {
            'username': auth_forms.UsernameField,
        }

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Username...',
                },
            ),

            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Email...',
                },
            ),

            'profile_image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Link to Image...',
                },
            ),

        }

        labels = {
            'profile_image_url': 'Profile Image URL',
        }
