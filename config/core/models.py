from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group

from datetime import datetime


# Group.objects.create(name='Doctor')
# Group.objects.create(name='Administrator')
# Group.objects.create(name='Receptionist')


class HospitalUser(AbstractUser):
    """Usuario del sistema

    registro de usuarios del sistema"""

    class Role(models.TextChoices):
        NONE = "NONE", "None"
        DOCTOR = "DOCTOR", "Doctor"
        ADMINISTRATOR = "ADMINISTRATOR", "Administrator"
        RECEPTIONIST = "RECEPTIONIST", "Receptionist"

    role = models.CharField(
        max_length = 50,
        choices = Role.choices,
        blank = False,
        null = False,
        default = Role.NONE
    )


class Doctor(models.Model):
    """Doctores que atienden las clinicas

    Cada doctor tiene un usuario para ingresar al sistema
    """


class MedicalUnit(models.Model):
    """Unidad medica a la que pertenece la clinica

    Args:
        models (_type_): _description_
    """


class Clinic(models.Model):
    """Clinica en la que se atienden los pacientes

    Args:
        models (_type_): _description_
    """


class Patient(models.Model):
    """Informacion del paciente, copiado diractamente de synthea

    Args:
        models (_type_): _description_
        id
        birthdate
        first
        last
        gender
    """

    class Gender(models.TextChoices):
        OTHER = 'O', "OTHER"
        MALE = 'M', "MALE"
        FEMALE = 'F', "FEMALE"

    name = models.CharField(
        max_length=250
    )

    paterno = models.CharField(
        max_length=250
    )

    materno = models.CharField(
        max_length=250,
        blank=True
    ) 

    birthdate = models.DateField(
        default=datetime.now, 
        blank=True
    )

    gender = models.CharField(
        max_length=1,
        choices=Gender.choices,
        null=False,
        blank=False,
        default=Gender.OTHER
    )



class Turn(models.Model):
    """Turno del pasiente en la filaPadtien

    Args:
        models (_type_): _description_
    """
    def emit(self, id):
        """Emitir turno

        Returns:
            _type_: _description_
        """
        pass


        

class Diagnostics(models.Model):
    """Diagnosticos del pasiente

    Args:
        models (_type_): _description_
    """
