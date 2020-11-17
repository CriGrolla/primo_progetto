from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#L1
def homepage(request):
    return render(request, "homepage.html")

#L2
def menu(request):
    return HttpResponse("<ol><li>Cristian</li><li>Grolla</li><li>19|03|02</li></ol>")

#L3
def chisiamo(request):
    return render(request, "chi_siamo.html")

#L4
def variabili(request):
    context= { 'var1': 'Cristian','var2': 'Grolla', 'var3' : '19|03|02'}
    return render(request, "variabili.html",context)

#L5
def index(request):
    return render(request, "index.html")
