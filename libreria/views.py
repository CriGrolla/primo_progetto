from django.shortcuts import render, get_object_or_404
from .models import Autore, Libro
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.
class LibroListView(ListView):
    model = Libro
    template_name = "lista_libri.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["libri"] = Libro.objects.all()
        return context


class AutoreDetail(DetailView):
    model=Autore
    template_name= "autore.html"