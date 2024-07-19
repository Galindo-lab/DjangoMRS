from django import forms
from .models import Activity

"""class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['name', 'start', 'end']
        widgets = {
            'start': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
"""