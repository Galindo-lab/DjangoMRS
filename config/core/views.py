from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from django.contrib.auth.models import User

from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404

from django.views.generic import TemplateView
from django.views import View

from .models import HospitalUser


def index(request: any) -> HttpResponse:
    return render(
        request=request,
        template_name='index.html'
    )


@login_required
def login_redirect(request: any) -> HttpResponse:
    match request.user.role:
        case HospitalUser.Role.ADMINISTRATOR:
            return HttpResponse("Tu eres admin")
        case HospitalUser.Role.DOCTOR:
            return HttpResponseRedirect('/clinic')
        case HospitalUser.Role.RECEPTIONIST:
            return HttpResponseRedirect('/reception')
        case _:
            return HttpResponseNotFound("No tienes permisos")


class Reception(LoginRequiredMixin, UserPassesTestMixin, View):
    login_url = '/login/'
    template_name = 'reception/main.html'
    view_role = HospitalUser.Role.RECEPTIONIST

    def test_func(self) -> bool:
        """Revisa si el usuario tiene el rol para la vista"""
        return self.request.user.role == self.view_role

    def get(self, request, *args, **kwargs) -> HttpResponse:
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs) -> HttpResponse:
        return render(request, self.template_name)


@login_required
def monitor(request: any) -> HttpResponse:
    return render(
        request=request,
        template_name='monitor.html'
    )


@login_required
def clinic(request: any) -> HttpResponse:
    return render(
        request=request,
        template_name='doctor/clinic.html'
    )
def Dashboard(request: any) -> HttpResponse:
    return render(
        request=request,
        template_name='Administrador/Dashboard.html'
    )

def Recepcion(request: any) -> HttpResponse:
    return render(
        request=request,
        template_name='Recepcionista/Recepcion.html'
    )

# class Login(View):
#     template_name = 'login.html'

#     def get(self, request, *args, **kwargs) -> HttpResponse:
#         print("a")
#         return render(request, self.template_name, {
#             'form': UserLoginForm()
#         })

#     def post(self, request, *args, **kwargs) -> HttpResponse:

#         print(request.user)

#         form = UserLoginForm(request.POST)

#         if form.is_valid():
#             print('c')
#             return HttpResponseRedirect('index')

#         # mostrar los errores en el form
#         print('d')
#         return render(request, self.template_name, {
#             'form': form
#         })
