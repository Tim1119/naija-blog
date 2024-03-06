from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .forms import SignUpForm,LoginForm
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout


class RegistrationView(SuccessMessageMixin,CreateView):
    form_class=SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('authentication:login') 
    success_message = 'your acccount has been succesfully created'

class LoginUser(LoginView):
    template_name = 'registration/login.html'
    authentication_form = LoginForm
    next_page = reverse_lazy('article:home')


@login_required
def UserLogoutView(request):
        
    logout(request)
    messages.success(request,'you have been logged out')
    return redirect('authentication:login')

