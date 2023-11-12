from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404

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
            return HttpResponse("Tu eres recepcionista")
        
        case _:
            return HttpResponseNotFound("No tienes permisos")

@login_required
def reception(request: any) -> HttpResponse:
    pass


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
