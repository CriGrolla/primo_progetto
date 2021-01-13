from django.urls import path
from .views import AutoreDetail_CG, LIBRO_CGListView

app_name='libreria'

urlpatterns=[
    #path("", home, name="homepage"),
    #path("articoli/<int:pk>", articoloDetailView, name="articolo_detail")
    #path("", AutoreDetail_CG, name="autore")
    path("autori/<int:pk>", AutoreDetail_CG.as_view(), name="autore"),
    path("lista_libri/", LIBRO_CGListView.as_view(), name="lista_libri"),
]