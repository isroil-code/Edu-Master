from django import forms
from . import models

class CourseForm(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = ('category','name','bio', 'price','author','image')
        
class LessonForm(forms.ModelForm):
    class Meta:
        model = models.Lesson
        fields = ('name', 'bio', 'video')
        
    
