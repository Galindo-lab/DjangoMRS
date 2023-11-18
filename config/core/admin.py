from django.contrib import admin

from .models import HospitalUser, MedicalUnit, Clinic, Patient, Turn


admin.site.register(HospitalUser)

admin.site.register(Patient)
admin.site.register(Turn)
admin.site.register(MedicalUnit)