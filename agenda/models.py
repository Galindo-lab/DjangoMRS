import datetime
import json

from django.contrib.auth.models import User
from django.db import models



class Agenda(models.Model):
    """
    Represents the agenda containing all other sections.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Contact(models.Model):
    """
    Represents a contact in the agenda.
    """
    agenda = models.ForeignKey(Agenda, related_name='contacs', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name


class RepeatChoices(models.TextChoices):
    NO_REPEAT = 'NR', 'Nunca'
    DAILY = 'DA', 'Diariamente'
    WEEKLY = 'WE', 'Semanalmente'
    MONTHLY = 'MO', 'Mensualmente'
    YEARLY = 'YE', 'Anualmente'


class Event(models.Model):
    """
    Represents an event in the calendar.
    """

    class Meta:
        ordering = ['start_time']

    agenda = models.ForeignKey(Agenda, related_name='events', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    contacts = models.ManyToManyField('Contact', related_name='events', blank=True)
    repeat = models.CharField(default=RepeatChoices.NO_REPEAT, choices=RepeatChoices.choices, max_length=2)
    all_day = models.BooleanField(default=False)

    def to_dict(self):
        return {
            'pk': self.pk,
            'title': self.title,
            'start': self.start_time,
            'end': self.end_time
        }

    def to_json(self):
        return json.dumps(self.to_dict())

    def __str__(self):
        return self.title
