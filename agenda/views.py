from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, UpdateView

from agenda.form import EventForm
from agenda.models import *


class PendingView(LoginRequiredMixin, View):
    def get(self, request):
        return render(
            request=request,
            template_name='agenda/agenda.html',
            context={
                "eventos": [a.to_dict() for a in Event.objects.all()]
            }
        )

pending_view = PendingView.as_view()


class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'agenda/event.html'
    success_url = reverse_lazy('index')  # Change this to your desired URL


event_update_view = EventUpdateView.as_view()


class EventCreateView(LoginRequiredMixin, FormView):
    template_name = 'agenda/event.html'
    success_url = reverse_lazy('index')
    form_class = EventForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.agenda = get_object_or_404(Agenda, user=self.request.user)
        obj.save()

        return super().form_valid(form)


event_view = EventCreateView.as_view()
