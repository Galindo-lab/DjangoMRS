from django import forms

from .models import Event


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'start_time', 'end_time', 'repeat', 'all_days']
