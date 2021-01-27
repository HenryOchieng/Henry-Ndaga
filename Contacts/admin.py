from django.contrib import admin
from .models import Contacts

# Register your models here.
#class ContactsAdmin(admin.ModelAdmin):
 #   list_display = ('name', 'email', 'subject','date',)
  #  search_fields = ('name', 'email',)
   # date_hierarchy = 'date'

admin.site.register(Contacts)
