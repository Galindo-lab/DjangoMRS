from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView, UpdateView

from agenda.form import EventForm
from agenda.models import *


def agenda_view(request):
    return render(
        request=request,
        template_name='agenda/agenda.html',
        context={
            "eventos": [a.to_dict() for a in Event.objects.all()]
        }
    )


class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'agenda/event.html'
    success_url = reverse_lazy('index')  # Change this to your desired URL


event_update_view = EventUpdateView.as_view()


class EventView(FormView):
    template_name = 'agenda/event.html'
    success_url = reverse_lazy('index')
    form_class = EventForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.agenda = get_object_or_404(Agenda, user=self.request.user)
        obj.save()

        return super().form_valid(form)


event_view = EventView.as_view()


# Create your views here.
def calendarView(request):
    return render(request, 'calendar_alphine.html', {
        'form': [a.to_dict() for a in Event.objects.all()],
        # 'activity_form': ActivityForm()
    })


"""
def item_list(request):
    items = Event.objects.all()
    return render(request, 'calendar_alphine.html', {'items': items})


def item_list_json(request):
    items = list(Event.objects.values())
    return JsonResponse(items, safe=False)
"""
