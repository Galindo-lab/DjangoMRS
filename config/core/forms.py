from django import forms
from django.contrib.auth.forms import AuthenticationForm

from . models import Patient, Doctor, Clinic, HospitalUser

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

# class ReceptionForm(forms.ModelForm):
#     class Meta:
#         model = Patient
#         # fields = []
