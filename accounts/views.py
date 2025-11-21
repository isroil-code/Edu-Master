from django.shortcuts import render, redirect
from django.views.generic import CreateView, View
from .forms import UserForm
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout

class RegisterView(CreateView):
    template_name = 'accounts/register.html'
    form_class = UserForm
    success_url = reverse_lazy('login')

class Logout(LoginRequiredMixin, View):
    def get(self, req):
        logout(req)
        return redirect('login')
        

    