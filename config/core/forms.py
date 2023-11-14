from django import forms
from django.contrib.auth.forms import AuthenticationForm

from . models import Patient, Doctor, Clinic, HospitalUser
from . models import MedicalUnit, Turn

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


class ReceptionForm(forms.Form):
    
    birthdate = forms.DateField()

    gender = forms.ChoiceField(
        choices=Patient.Gender.choices
    )

    name = forms.CharField(
        max_length=250
    )

    paterno = forms.CharField(
        max_length=250
    )

    materno = forms.CharField(
        max_length=250
    )

    medical_unit = forms.CharField(
        max_length=250,
    )

    def patient(self) -> list:
        """Regresa una lista de pacientes con los mismos datos"""
        return Patient.objects.filter(
            name=self.cleaned_data['name'],
            paterno=self.cleaned_data['paterno'],
            materno=self.cleaned_data['materno'],
            birthdate=self.cleaned_data['birthdate'],
        )
    
    def unit(self) -> list:
        """Regresa una lista de unidades medicas con el mismo nombre"""
        return MedicalUnit.objects.filter(
            name=self.cleaned_data['medical_unit']
        )
