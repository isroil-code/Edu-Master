from django.contrib import admin
from .models import Category,Comment, CommentLike, Course,Lesson,Like, StudentCourses

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(StudentCourses)

