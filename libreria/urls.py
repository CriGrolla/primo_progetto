from django.urls import path
from .views import AutoreDetail, LibroListView

app_name='libreria'

urlpatterns=[
    #path("", home, name="homepage"),
    #path("articoli/<int:pk>", articoloDetailView, name="articolo_detail")
    #path("", AutoreDetail, name="autore")
    path("autori/<int:pk>", AutoreDetail.as_view(), name="autore"),
    path("lista_libri/", LibroListView.as_view(), name="lista_libri"),
]