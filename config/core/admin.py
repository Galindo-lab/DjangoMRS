from django.contrib import admin

from .models import HospitalUser, Doctor, MedicalUnit, Clinic, Patient

# Register your models here.

admin.site.register(HospitalUser)
