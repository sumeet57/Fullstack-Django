from django.db import models
from auth_app.models import User

# Create your models here.

class Task(models.Model):
    title = models.TextField(max_length=100, default='none empty')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

