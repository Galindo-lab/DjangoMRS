# Generated by Django 4.2.5 on 2023-11-12 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_patient_birthdate_patient_first_patient_gender_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='last',
            new_name='paterno',
        ),
        migrations.AddField(
            model_name='patient',
            name='materno',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
