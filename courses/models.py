from django.db import models
from accounts.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    bio = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.CharField(max_length=200)
    rate = models.DecimalField(max_digits=5, decimal_places=0, null=True, blank=True)
    image = models.ImageField(upload_to='course_images/')
    
    def __str__(self):
        return self.name
    
class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    name = models.CharField(max_length=200)
    bio = models.TextField()
    rate = models.DecimalField(max_digits=5, decimal_places=0, null=True, blank=True)
    video = models.FileField(upload_to='lesson_files/')
    
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    texted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username

class Like(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.IntegerField(default=0)
    liked_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    
class CommentLike(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.IntegerField(default=0)
    liked_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    
class StudentCourses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_courses')
    courses = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='student_courses')
    is_active = models.BooleanField(default=False)
    bought_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    
    