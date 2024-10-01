from django.urls import path
from .views import recipe_create , recipe_delete, recipe_update

urlpatterns = [
    path('create/', recipe_create, name='recipe_create'),
    path('delete/<int:id>/', recipe_delete, name='recipe_delete'),
    path('update/<int:id>/', recipe_update, name='recipe_update'),
]