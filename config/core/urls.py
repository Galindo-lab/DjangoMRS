from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . forms import UserLoginForm
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', LoginView.as_view(
        template_name='login.html',
        authentication_form=UserLoginForm
    ), name='login'),

    #path('login', views.Login.as_view(), name='login')
]
