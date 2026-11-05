from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def blog(request):
    return HttpResponse("<h4>barevvv<h4/>")

def create(request):
    return HttpResponse("<h4>barevvv dzezz<h4/>")