from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import signup


urlpatterns = [
    path('', signup, name='signup'),
]
