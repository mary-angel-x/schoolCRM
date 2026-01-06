from django.contrib.auth.models import AbstractUser # это нужно для расширения стандартной модели пользователя
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')


