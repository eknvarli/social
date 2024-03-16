from django.urls import path
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

def login(request, *args, **kwargs):
    if request.user.is_authenticated and request.path == reverse_lazy('login'):
        return HttpResponseRedirect(reverse_lazy('index'))
    else:
        return LoginView.as_view(template_name='social/login.jinja')(request, *args, **kwargs)