from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

from . models import Doctor


class UserLoginForm(AuthenticationForm):
    """_summary_

    Args:
        AuthenticationForm (_type_): _description_
    """

    username = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nombre'
            }
        )
    )

    password = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            'type': 'password',
            'class': 'form-control',
            'placeholder': 'Contraseña'
        })
    )
