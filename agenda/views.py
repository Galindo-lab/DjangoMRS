from django.shortcuts import render

from agenda.form import ActivityForm
from agenda.models import Activity
    

# Create your views here.
def calendarView(request):
    return render(request, 'calendar.html', {
        'form': [a.to_dict() for a in Activity.objects.all()],
        'activity_form': ActivityForm()
    })
