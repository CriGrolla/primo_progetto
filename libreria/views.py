from django.shortcuts import render, get_object_or_404
from .models import AUTORE_CG, LIBRO_CG
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.
class LIBRO_CGListView(ListView):
    model = LIBRO_CG
    template_name = "lista_libri.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["libri"] = LIBRO_CG.objects.all()
        return context


class AutoreDetail_CG(DetailView):
    model=AUTORE_CG
    template_name= "autore.html"