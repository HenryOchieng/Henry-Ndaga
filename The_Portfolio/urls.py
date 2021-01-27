from django.urls import path

from .import views

urlpatterns = [
    path('',views.The_Portfolio,name='The_Portfolio'),
    path('Home',views.Home, name="Home")
]