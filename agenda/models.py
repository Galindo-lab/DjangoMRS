import json

from django.db import models
import datetime


# Create your models here.
class Activity(models.Model):
    name = models.CharField(max_length=255)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def to_dict(self):
        return {
            'name': self.name,
            'start': self.start,
            'end': self.end
        }

    def to_json(self):
        return json.dumps(self.to_dict())

    def __str__(self):
        return self.name
