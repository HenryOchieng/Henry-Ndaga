from django.shortcuts import render

from django.http import HttpResponse

from .models import The_Portfolio

# Create your views here.

def index(request):
    portfolios = The_Portfolio.objects
    return render(request,'The_Portfolio/index.html')

def Home(request):
    return render(request,'Home/main.html')
