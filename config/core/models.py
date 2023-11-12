from django.db import models

from django.contrib.auth.models import AbstractUser


class HospitalUser(AbstractUser):
    """Usuario del sistema

    registro de usuarios del sistema"""

    class Role(models.TextChoices):
        NONE = "NONE", "None"
        DOCTOR = "DOCTOR", "Doctor"
        ADMINISTRATOR = "ADMINISTRATOR", "Administrator"
        RECEPTIONIST = "RECEPTIONIST", "Receptionist"

    role = models.CharField(
        max_length=50,
        choices=Role.choices,
        blank=False,
        null=False,
        default=Role.NONE
    )

    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         return super().save(*args, **kwargs)


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
        deathdate
        ssn
        drivers
        passport
        prefix
        first
        last
        suffix
        maiden
        marital
        race
        ethnicity
        gender
        birthplace
        address
        city
        state
        county
        fips
        zip
        lat
        lon
        healthcare_expenses
        healthcare_coverage
        income
    """



class Turn(models.Model):
    """Turno del pasiente en la fila

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
