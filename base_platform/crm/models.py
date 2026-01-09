from django.db import models

# файл для модели 
# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

