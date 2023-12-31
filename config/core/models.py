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



class DoctorsOffice(models.Model):
    """Consultorio del medico"""
    doctor = models.ForeignKey(
        to=HospitalUser,
        on_delete=models.CASCADE,
        null=True,
    )
    
    patien = models.ForeignKey(
        to=Patient,
        on_delete=models.CASCADE,
    )


class MedicalUnit(models.Model):
    """Unidad medica a la que pertenece la clinica

    Args:
        models (_type_): _description_
    """

    class Priority(models.IntegerChoices):
        """Niveles de urgencia de la unidad medica"""
        HIGH = 0, "Alto"
        MEDIUM = 1, "Medio"
        LOW = 2, "Bajo"

    name = models.CharField(
        max_length=250,
        primary_key=True
    )

    priority = models.IntegerField(
        choices=Priority.choices,
        default=Priority.LOW
    )



class Clinic(models.Model):
    """Clinica en la que se atienden los pacientes

    Args:
        models (_type_): _description_
    """

class Turn(models.Model):
    """Modelo de turno para el paciente"""

    patient = models.OneToOneField(
        to=Patient,
        on_delete=models.CASCADE
    )

    emited = models.DateTimeField(
        default=datetime.now
    )

    medical_unit = models.ForeignKey(
        to=MedicalUnit,
        on_delete=models.CASCADE,
        blank=True, 
        null=True
    )

    # TODO falta la clinica
    
    def next() -> 'Turn':
        """Retorna el siguiente turno"""
        return Turn.objects.order_by(
            'emited'
        ).first()
        

class Diagnostics(models.Model):
    """Diagnosticos del pasiente

    Args:
        models (_type_): _description_
    """
