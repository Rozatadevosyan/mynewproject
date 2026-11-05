

from django.conf.urls import handler400
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "main/index.html")

def about(request):
    return render(request, "main/about.html")

def contact(request):
    return render(request, "main/contact.html")

def profile(request):
    return HttpResponse("<h4>Vopshm apehhhh</h4>")