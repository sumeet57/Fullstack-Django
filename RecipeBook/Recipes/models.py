from django.db import models
from auth_app.models import User

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    ingredients = models.TextField(max_length=500)
    instructions = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title