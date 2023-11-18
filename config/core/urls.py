from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . forms import UserLoginForm

from . import views
from .views import ReceptionView, ClinicView

urlpatterns = [
    path(
        route='login/',
        name='login',
        view=LoginView.as_view(
            template_name='login.html',
            authentication_form=UserLoginForm
        )
    ),
    path(
        route='logout/',
        name='logout',
        view=LogoutView.as_view()
    ),
    path(
        route='',
        name='index',
        view=views.index
    ),
    path(
        route='loginRedirect/',
        name='loginRedirect',
        view=views.login_redirect
    ),
    path(
        route='monitor/',
        name='monitor',
        view=views.monitor
    ),
    path(
        route='clinic/',
        name='clinic',
        view=ClinicView.as_view()
    ),
    path(
        route='Dashboard/',
        name='Dashboard',
        view=views.Dashboard
    ),
    path(
        route='reception/',
        name='reception',
        view=ReceptionView.as_view()
    ),
]
