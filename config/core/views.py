from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin

from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404

from django.views.generic import TemplateView
from django.views import View

from .models import HospitalUser
from .models import Patient
from .models import Turn

from .forms import ReceptionForm


def index(request: any) -> HttpResponse:
    return render(
        request=request,
        template_name='index.html'
    )


@login_required
def login_redirect(request: any) -> HttpResponse:
    """Redirige al usuario a su vista dependiendo del rol"""
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
    template_name = 'reception/recepcion.html'
    view_role = HospitalUser.Role.RECEPTIONIST

    def test_func(self) -> bool:
        """Revisa si el usuario tiene el rol para la vista"""
        return self.request.user.role == self.view_role

    def get(self, request, *args, **kwargs) -> HttpResponse:
        """Muestra el formulario"""
        return render(request, self.template_name, {
            "form": ReceptionForm()
        })

    def post(self, request, *args, **kwargs) -> HttpResponse:
        """Recibe el formulario"""
        patient_form = ReceptionForm(request.POST)

        if not patient_form.is_valid():
            return HttpResponseNotFound("Formulario invalido")

        if not patient_form.found():
            return HttpResponseNotFound("Paciente no encontrado")

        patient = Patient.objects.filter(
            name=patient_form.cleaned_data['name'],
            paterno=patient_form.cleaned_data['paterno'],
            materno=patient_form.cleaned_data['materno'],
            birthdate=patient_form.cleaned_data['birthdate'],
        )[0]

        turn = Turn(
            patient=patient
        )

        turn.save()

        return HttpResponse("valido")


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


@login_required
def Dashboard(request: any) -> HttpResponse:
    return render(
        request=request,
        template_name='Administrador/Dashboard.html'
    )
