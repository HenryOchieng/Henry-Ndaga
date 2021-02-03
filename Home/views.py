from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from .models import Home

# Create your views here.

class HomeView(TemplateView):
    template_name = "Home/index.html"
    def Home(self):
        return render('Home/index.html')
class AboutView(TemplateView):
    template_name = "About/index.html"
#def Home(request):
 #   return render(request,'Home/index.html')

#def About(request):
 #   return render(request, 'About/index.html')

#def The_Portfolio(request):
 #   return render(request, 'The_Portfolio/index.html')

#def Contacts(request):
 #   return render(request, 'Contacts/index.html')