from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    # age = models.PositiveIntegerField()
    profile_image = models.ImageField(upload_to='profile_images/', blank=True)

    def __str__(self):
        return self.username
