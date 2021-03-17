from django.contrib import admin
from django.urls import path, include
from .views import contatti

urlpatterns = [
    path('contattaci/', contatti, name='contatti'),
]