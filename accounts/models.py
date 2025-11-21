from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    CHOICE_ROLE = [
        ('STUDENT', 'STUDENT'),
        ('TEACHER', 'TEACHER'),
        ('ADMIN','ADMIN')
    ]
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=200)
    phone = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='profile-images/')
    country = models.CharField(max_length=200, null=True, blank=True)
    role = models.CharField(max_length=200, choices=CHOICE_ROLE, default='STUDENT')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)
     
    def __str__(self):
        return self.username
    
    

    
