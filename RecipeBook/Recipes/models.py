from django.db import models

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    ingredients = models.TextField(max_length=500)
    instructions = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='images/')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title