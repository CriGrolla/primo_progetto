from django.contrib import admin

# Register your models here.
from .models import Genere, Autore, Libro

admin.site.register(Genere)
admin.site.register(Autore)
admin.site.register(Libro)