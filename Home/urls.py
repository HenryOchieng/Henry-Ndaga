from django.urls import path

from .import views

urlpatterns = [
    path('', views.Home, name="Home"),
    path('About', views.About, name="About"),
    path('The_Portfolio', views.The_Portfolio, name="The_Portfolio"),
    path('Contacts', views.Contacts, name="Contacts")
]