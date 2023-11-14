from django.core.management.base import BaseCommand
from core.models import MedicalUnit


class Command(BaseCommand):
    def handle(self, **options):
        MedicalUnit(
            name = "Unidad 1",
            priority = MedicalUnit.Priority.LOW
        ).save()

        MedicalUnit(
            name="Unidad 2",
            priority = MedicalUnit.Priority.MEDIUM
        ).save()

        MedicalUnit(
            name = "Unidad 3",
            priority = MedicalUnit.Priority.HIGH
        ).save()

