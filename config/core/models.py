from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Doctor(models.Model):
    """Doctores que atienden las clinicas

    Args:
        models (_type_): _description_
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


class PatientTurn(models.Model):
    """Turno del pasiente en la fila

    Args:
        models (_type_): _description_
    """


class PatientData(models.Model):
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
