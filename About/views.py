from django.shortcuts import render

from django.http import HttpResponse

from .models import About

# Create your views here.
def index(request):
   # abouts = About.objects
    return render(request,'About/index.html')

def Home(request):
   return render(request,'Home/index.html')  

