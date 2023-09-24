from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404

from . forms import UserLoginForm

def index(request: any) -> HttpResponse:
    """_summary_

    Args:
        request (any): _description_

    Returns:
        HttpResponse: _description_
    """
    
    return render(
        request=request,
        template_name='index.html'
    )


def login(request :any) -> HttpResponse:
    """_summary_

    Args:
        request (any): _description_

    Returns:
        HttpResponse: _description_
    """
    return render(request, 'login.html', {
       'form': UserLoginForm()
    })
    