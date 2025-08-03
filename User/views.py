from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordResetView
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm

# Create your views here.
def views_index(request):
    return render(request, 'base.html')

def views_home(request):
    if not request.user.is_authenticated:
        return redirect('user:login')
    return render(request, 'home.html')

def views_user_registration(request):
    context = {}
    if request.POST:
        form = forms_user_registration(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password1']
            user = authenticate(email=email, password=password)
            login(request, user)
            messages.info(request, 'The username ' + username + ' has been successfully created!')
            return redirect('user:home')
        else:
            context['form'] = forms_user_registration()
    else:
        form = forms_user_registration()
        context['form'] = forms_user_registration
    return render(request, 'register.html', context)

def views_login(request):
    context = {}
    if request.POST:
        try:
            form = forms_login(request.POST)
            if form.is_valid():
                email = request.POST['email']
                password = request.POST['password']
                user = authenticate(email=email, password=password)
                login(request, user)
                messages.info(request, request.user)
                return redirect('user:home')
            else:
                messages.info(request, 'Wrong in email & password')
                context['login_form'] = forms_login
        except models_user_registration.DoesNotExist:
            messages.info(request, "Email doesn't exixt")
            return redirect('user:index')
    else:
        form = forms_login()
        context['login_form'] = form
    return render(request, 'login.html', context)

def views_logout(request):
    logout(request)
    return redirect('user:login')

# Create your views here.
class view_passwordChange( PasswordChangeView):
    form = PasswordChangeForm
    template_name='password_change.html'
    success_url = reverse_lazy('user:home')
    success_message = "Password Successfully changed"

class view_passwordReset(PasswordResetView):
    form = PasswordResetForm
    template_name = 'password_reset_form.html'