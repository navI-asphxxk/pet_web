from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django import forms

User = get_user_model()


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(label='email')
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    phone = forms.CharField(label='phone')
    first_name = forms.CharField(label='first_name')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("first_name", "email", "phone")
        field_classes = {"first_name": UsernameField,

                         }
