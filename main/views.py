from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, FormView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from courses.models import Course
from accounts.permissions import IsAdminMixin, IsStudentMixin, IsTeacherMixin
from courses.models import Course, Category
from .forms import CommentForm
from courses.models import Lesson

class IndexView(ListView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
    template_name = 'main/home_new.html'
    queryset = Course.objects.all()
    context_object_name = 'courses'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class HomeView(LoginRequiredMixin,ListView):
    template_name = 'main/home.html'
    queryset = Course.objects.all()
    context_object_name = 'courses'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('q', '')
        
        if search:
            queryset = Course.objects.filter(name__icontains=search)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class Contact(LoginRequiredMixin,TemplateView):
    template_name = 'main/contact.html'
    
class About(LoginRequiredMixin,TemplateView):
    template_name = 'main/about.html'
    
class Blog(LoginRequiredMixin,TemplateView):
    template_name = 'main/blog.html'
      
