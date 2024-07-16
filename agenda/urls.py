from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from agenda.views import calendarView

urlpatterns = [
    path(route='', name='index', view=calendarView),
]
