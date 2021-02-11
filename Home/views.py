from django.shortcuts import render
from django.http import HttpResponse
from .models import Home

def Home(request):
    return render(request,'Home/main.html')

def About(request):
    return render(request, 'About/index.html')

def The_Portfolio(request):
    return render(request, 'The_Portfolio/index.html')

def Contacts(request):
    return render(request, 'Contacts/index.html')