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


class ReceptionForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            "birthdate",
            "gender",
            "name",
            "paterno",
            "materno"
        ]

    def patient(self) -> list:
        """Regresa una lista de pacientes con los mismos datos"""
        return Patient.objects.filter(
            name=self.cleaned_data['name'],
            paterno=self.cleaned_data['paterno'],
            materno=self.cleaned_data['materno'],
            birthdate=self.cleaned_data['birthdate'],
        )

    def found(self) -> bool:
        """Regresa si el paciente ya existe en la base de datos"""
        return self.patient().exists()