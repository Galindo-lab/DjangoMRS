from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . forms import UserLoginForm
from . import views

urlpatterns = [
    path(
        route='',
        name='index',
        view=views.index
    ),
    path(
        route='login/',
        name='login',
        view=LoginView.as_view(
            template_name='login.html',
            authentication_form=UserLoginForm
        )
    ),
    path(
        route='monitor/',
        name='monitor',
        view=views.monitor
    ),
    path(
        route='clinic/',
        name='clinic',
        view=views.clinic
    ),
    path(
        route='Dashboard/',
        name='Dashboard',
        view=views.Dashboard
    ),
    path(
        route='Recepcion/',
        name='Recepcion',
        view=views.Recepcion
    )
]
