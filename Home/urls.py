from django.urls import path, reverse
#from . import HomeView
from django.views.generic import TemplateView

from .import views

urlpatterns = [
    #path('', views.Home, name="Home"),
    path('', TemplateView.as_view(template_name = "Home/index.html")),
    #path('About', TemplateView.as_view(template_name = "About/index.html")),
    path('About', views.About, name="About"),
    path('The_Portfolio', views.The_Portfolio, name="The_Portfolio"),
    path('Contacts', views.Contacts, name="Contacts")
]