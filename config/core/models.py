from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group

from datetime import datetime


# Group.objects.create(name='Doctor')
# Group.objects.create(name='Administrator')
# Group.objects.create(name='Receptionist')


class HospitalUser(AbstractUser):
    """Usuario del sistema

    registro de usuarios del sistema
    """

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

    class Priority(models.IntegerChoices):
        """Niveles de urgencia de la unidad medica"""
        ALTO = 0, "Alto"
        MEDIO = 1, "Medio"
        BAJO = 2, "Bajo"

    name = models.CharField(
        max_length=250
    )

    priority = models.IntegerField(
        choices=Priority.choices,
        default=Priority.BAJO
    )



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
        OTHER = 'O', "Indefinido"
        MALE = 'M', "Masculino"
        FEMALE = 'F', "Femenino"

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

    def has_turn(self) -> bool:
        """Regresa si el paciente tiene un turno"""
        return Turn.objects.filter(
            patient=self
        )



class Turn(models.Model):
    """Modelo de turno para el paciente"""

    patient = models.OneToOneField(
        to=Patient,
        on_delete=models.CASCADE
    )

    emited = models.DateTimeField(
        default=datetime.now
    )

    # TODO falta la clinica
    
    def create(self, patient: Patient):
        Turn.objects.create(
            patient=patient
        )

        

class Diagnostics(models.Model):
    """Diagnosticos del pasiente

    Args:
        models (_type_): _description_
    """
