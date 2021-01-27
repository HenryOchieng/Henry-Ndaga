from django.shortcuts import render

from django.http import HttpResponse


from .models import Home

# Create your views here.

def Home(request):
   # homes = Home.objects
    return render(request,'Home/index.html',{'Home':Home})

def About(request):
    return render(request, 'About/index.html')

def The_Portfolio(request):
    return render(request, 'The_Portfolio/index.html')

def Contacts(request):
    return render(request, 'Contacts/index.html')