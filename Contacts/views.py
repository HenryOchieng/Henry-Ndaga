from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Contacts
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib import messages
#from django.forms import ContactsForm
#from .forms import ContactsForm

# Create your views here.  
#def Contacts(request):
def Contacts(request):
    if request.method == 'POST':
       # f = ContactsForm(request.POST)
        #if f.is_valid():
         #   f.save()
        messages.add_message(request, messages.INFO, 'Feedback Submitted.')
        return redirect('feedback')
    #else:
       # f = ContactsForm()
    return render(request, 'Contacts/index.html', {})


def Home(request):
   return render(request,'Home/main.html')






