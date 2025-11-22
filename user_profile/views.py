from django.shortcuts import render
from django.views.generic import DetailView, CreateView, UpdateView
from accounts.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfileForm
from django.urls import reverse_lazy

class Profile(LoginRequiredMixin, DetailView):
    template_name = 'user_profile/profile.html'
    model = User
    context_object_name = 'user'
    
    def get_object(self):
        return self.request.user
    
class UpdateProfile(LoginRequiredMixin, UpdateView):
    template_name = 'user_profile/update_profile.html'
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('user-profile')
    
    def get_object(self):
        return self.request.user
    
    def form_valid(self, form):
        return super().form_valid(form)