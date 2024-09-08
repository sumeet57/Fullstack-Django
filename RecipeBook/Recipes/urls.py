from django.urls import path, include
from .views import recipes, details

urlpatterns = [
    path('', recipes , name='recipes'),
    path('detail/<int:id>', details, name='details'),
]