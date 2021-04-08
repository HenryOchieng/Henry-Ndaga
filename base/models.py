from __future__ import unicode_literals

from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField(max_length=200)
    tools = models.CharField(max_length=100) # space-separated values
    pub_date = models.DateTimeField()
    img_name = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=200, help_text="Name of the sender")
    email = models.EmailField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Contact"

    def __str__(self):
        return self.name + "-" +  self.email