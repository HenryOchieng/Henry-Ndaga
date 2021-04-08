from django.urls import path
from .views import ProjectListAndFormView

urlpatterns = [
    path('', ProjectListAndFormView.as_view(), name='base'),
    #path('', Home.as_view(), name='home'),
    #path('about/', About.as_view(), name='about'),
    #path('hire_me/', Contact.as_view(), name='hire'),
    #path('portfolio', Portfolio.as_view(), name='portfolio'),
]