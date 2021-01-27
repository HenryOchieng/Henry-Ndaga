from django.urls import path, include

from .import views


urlpatterns = [
    path('Contacts',views.Contacts,name='Contact'),
    #path('feedback', views.feedback, name='Feedback'),
    path('Home',views.Home,name="Home")
    
]