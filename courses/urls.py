from django.urls import path
from . import views

urlpatterns = [
    path('create-course/', views.CreateCourse.as_view(), name='course-create'),
    path('update-course/<int:pk>/', views.CourseUpdate.as_view(), name='update-course'),
    path('delete-course/<int:pk>/', views.CourseDelete.as_view(), name='delete-course'),
    path('teacher-courses/' ,views.TeacherCourses.as_view(), name='teacher-courses'),
    path('add-lesson/<int:pk>/', views.AddLesson.as_view(), name='add-lesson'),
    path('lessons/<int:pk>/', views.Lessons.as_view(), name='lessons'),
    path('verify/<int:pk>/', views.code_generator, name='verify'),
    path('buy-course/', views.BuyCourse, name='buy-course'),
    path('student-courses/', views.StudentCourse.as_view(),name='student-courses'),
    path('course-detail/<int:pk>/', views.CourseDetail.as_view(), name='course-detail'),
    path('write-comment/<int:pk>/', views.WriteComment.as_view(), name='write-comment')
    
]