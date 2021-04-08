from __future__ import unicode_literals

from django.contrib import admin
from .models import Project, Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date',)
    search_fields = ('name', 'email',)
    date_hierarchy = 'date'

admin.site.register(Project)
admin.site.register(Contact, ContactAdmin)