from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from agenda.views import *

urlpatterns = [
    path(route='', name='index', view=calendarView),
    path('items/', item_list, name='item_list'),
    path('api/items/', item_list_json, name='item_list_json'),
]
