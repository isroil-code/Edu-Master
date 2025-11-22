from django.urls import path
from . import views

urlpatterns = [
    path('user-profile/', views.Profile.as_view(), name='user-profile'),
    path('update-profile/', views.UpdateProfile.as_view(), name='update-profile')
]