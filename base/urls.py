from django.urls import path
from .views import ProjectListAndFormView

urlpatterns = [
    path('', ProjectListAndFormView.as_view(), name='base'),
]