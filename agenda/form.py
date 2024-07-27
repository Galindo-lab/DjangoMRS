from django import forms

from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'start_time', 'end_time', 'repeat', 'all_day']


class SelectDate(forms.Form):
    date = forms.DateField()