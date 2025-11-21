from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('blog/', views.Blog.as_view(), name='blog'),
    path('contact/', views.Contact.as_view(), name='contact')
]