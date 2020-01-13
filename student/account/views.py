from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from .forms import SingUpForm, LoginForm
from django.contrib.auth import logout
# Create your views here.


def home(request):
    return render(request, 'account/home.html')


class SignUpView(FormView):
    form_class = SingUpForm
    template_name = 'account/sing_up.html'
    success_url = '/account/home'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'account/login.html'
    success_url = '/account/home'

    def form_valid(self, form):
        form.log(self.request)
        return super().form_valid(form)


def logout_user(request):
    logout(request)
    return redirect('/account/home')
