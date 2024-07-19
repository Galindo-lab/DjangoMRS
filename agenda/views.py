from django.http import JsonResponse
from django.shortcuts import render

# from agenda.form import ActivityForm
from agenda.models import *


# Create your views here.
def calendarView(request):
    return render(request, 'calendar_alphine.html', {
        'form': [a.to_dict() for a in Event.objects.all()],
        # 'activity_form': ActivityForm()
    })


def item_list(request):
    items = Event.objects.all()
    return render(request, 'calendar_alphine.html', {'items': items})


def item_list_json(request):
    items = list(Event.objects.values())
    return JsonResponse(items, safe=False)
