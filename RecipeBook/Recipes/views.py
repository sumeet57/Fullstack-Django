from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe

# Create your views here.

def recipes(request):
    return render(request, 'recipes.html', {'recipes': Recipe.objects.all(), 'len': len(Recipe.objects.all())})

def details(request, id):
    return render(request, 'details.html', {'recipe': Recipe.objects.get(id=id)})