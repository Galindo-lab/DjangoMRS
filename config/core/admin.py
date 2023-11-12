from django.contrib import admin

from .models import HospitalUser, Doctor, MedicalUnit, Clinic, Patient


admin.site.register(HospitalUser)

admin.site.register(Patient)