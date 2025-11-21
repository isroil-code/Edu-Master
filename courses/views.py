from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.views.generic import CreateView, ListView, RedirectView, UpdateView, DeleteView, DetailView
from .forms import CourseForm, LessonForm
from django.urls import reverse_lazy
from accounts.permissions import IsAdminMixin, IsStudentMixin, IsTeacherMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Course
from django.views import View
from django.contrib import messages
from django.core import exceptions
from django.core.mail import send_mail
import random
from .models import StudentCourses, Comment, Lesson
from django.contrib.auth.decorators import login_required
from main.forms import CommentForm

class CreateCourse(LoginRequiredMixin, IsTeacherMixin, CreateView):
    model = Course
    template_name = 'courses/course_create.html'
    form_class = CourseForm
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.files.image = self.request.FILES
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'create'
        return context
    

class CourseUpdate(LoginRequiredMixin, IsTeacherMixin,UpdateView):
    model = Course
    template_name = 'courses/course_create.html'
    form_class = CourseForm
    success_url = reverse_lazy('home')
    
    
    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'update'
        return context
    
class CourseDelete(LoginRequiredMixin,IsTeacherMixin, View):
    def get(self, req, pk):
        course = get_object_or_404(Course, pk=pk)
        course.delete()
        return redirect('home')
        

# --- Teacher views -----

class TeacherCourses(LoginRequiredMixin,IsTeacherMixin, ListView):
    template_name = 'courses/teacher_courses.html'
    queryset = Course.objects.all()
    context_object_name = 'courses'
    
    def get_queryset(self):
        queryset = self.queryset
        queryset = queryset.filter(user=self.request.user)
        return queryset

class AddLesson(LoginRequiredMixin, IsTeacherMixin, CreateView):
    template_name = 'courses/lesson.html'
    form_class = LessonForm
    success_url = reverse_lazy('teacher-courses')
    
    def form_valid(self, form):
        course_id = self.kwargs['pk']
        form.instance.course = Course.objects.get(id=course_id)
        return super().form_valid(form)
    
class Lessons(LoginRequiredMixin, DetailView):
    template_name = 'courses/lessons.html'
    queryset = Course.objects.all()
    context_object_name = 'courses'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lesson_pk = self.kwargs['pk']
        course = Course.objects.get(pk=lesson_pk)
        context['comments'] = Comment.objects.filter(course=course)
        return context
    
    
class WriteComment(LoginRequiredMixin, CreateView):
    template_name = 'courses/comments.html'
    form_class = CommentForm
    success_url = reverse_lazy('student-courses')
    
    def form_valid(self, form):
        course = Course.objects.get(pk=self.kwargs['pk'])
        form.instance.user = self.request.user
        form.instance.course = course
        return super().form_valid(form)
    

def code_generator(req,pk):
    if req.method == 'POST':
        password = ''
        code = [random.randint(0,9) for i in range(6)]
        for i in code:
            password += str(i)
        send_mail(
                subject='Salom!',
                message=f'Tasdiqlash Kodi: {password}',
                from_email='isroilberdiyorov3@gmail.com',
                recipient_list=[req.user.email],
                fail_silently=False,
                )
        req.session['code'] = password
        req.session['pk'] = pk
        return redirect('buy-course')
    return render(req, 'courses/verify.html')
    
    
@login_required
def BuyCourse(req):
        password = req.session.get('code')
        pk = req.session.get('pk')
        if req.method == 'POST':
            courses = get_object_or_404(Course, pk=pk)
            
            user_password = req.POST.get('code')
            if not str(user_password) == str(password):
                return render(req, 'courses/buy_course.html',{'error':'Wrong code'})
        
            StudentCourses.objects.create(user=req.user, courses=courses, is_active=True)
            return redirect('home')
        return render(req, 'courses/buy_course.html')
    

class StudentCourse(LoginRequiredMixin, IsStudentMixin or IsAdminMixin, ListView):
    template_name = 'courses/student_courses.html'
    queryset = StudentCourses.objects.all()
    context_object_name = 'courses'
    
    def get_queryset(self):
        queryset = self.queryset
        queryset = queryset.filter(user=self.request.user)
        return queryset
    
class CourseDetail(LoginRequiredMixin,DetailView):
    template_name = 'main/course_detail.html'
    queryset = Course.objects.all()
    context_object_name = 'course'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = Course.objects.get(pk=self.kwargs['pk'])
        context['comments'] = Comment.objects.filter(course=course)
        return context

    def dispatch(self, request, *args, **kwargs):
        course = self.get_object()
        if request.user.is_authenticated:
            if StudentCourses.objects.filter(user=request.user, courses=course, is_active=True).exists():
                return redirect('student-courses')
        if request.user.is_authenticated:
            if request.user.role == 'TEACHER':
                return redirect('teacher-courses')
        return super().dispatch(request, *args, **kwargs)
    
