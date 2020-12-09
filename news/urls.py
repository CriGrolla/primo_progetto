from django.urls import path
from .views import home, articoloDetailViewCB #articoloDetailView

app_name='news'

urlpatterns=[
    path("", home, name="homeview"),
    #path("articoli/<int:pk>", articoloDetailView, name="articolo_detail")
    path("articoli/<int:pk>", articoloDetailViewCB.as_view(), name="articolo_detail"),
]