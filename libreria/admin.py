from django.contrib import admin

# Register your models here.
from .models import GENERE_CG, AUTORE_CG, LIBRO_CG

admin.site.register(GENERE_CG)
admin.site.register(AUTORE_CG)
admin.site.register(LIBRO_CG)