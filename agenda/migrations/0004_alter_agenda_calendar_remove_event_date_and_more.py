# Generated by Django 5.0.6 on 2024-07-21 03:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0003_delete_activity'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='calendar',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='description',
        ),
        migrations.AddField(
            model_name='event',
            name='all_day',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='repeat',
            field=models.CharField(choices=[('NR', 'No se repite'), ('DA', 'Diario'), ('WE', 'Semanal'), ('MO', 'Mensual'), ('YE', 'Anual')], default='NR', max_length=2),
        ),
        migrations.DeleteModel(
            name='Calendar',
        ),
    ]
