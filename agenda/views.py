from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.views import View
from django.views.generic import FormView, UpdateView

from agenda.form import EventForm, SelectDate
from agenda.models import *


class PendingView(LoginRequiredMixin, View):
    def get(self, request):
        current_year = now().year

        return render(
            request=request,
            template_name='agenda/agenda.html',
            context={
                "selectDate": SelectDate(),
                "eventos": [a.to_dict() for a in Event.filter_by_year(current_year)]
            }
        )

    def post(self, request):
        form = SelectDate(request.POST)

        if form.is_valid():
            date = form.cleaned_data['date']
            year = date.year

            return render(
                request=request,
                template_name='agenda/agenda.html',
                context={
                    "selectDate": SelectDate(),
                    "eventos": [a.to_dict() for a in Event.filter_by_year(year)]
                }
            )




pending_view = PendingView.as_view()


class AgendaDay(LoginRequiredMixin, View):
    def get(self, request):
        return render(
            request=request,
            template_name='agenda/agenda_dia.html',
            context={
                "eventos": [a.to_dict() for a in Event.objects.all()]
            }
        )


agenda_day_view = AgendaDay.as_view()


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
