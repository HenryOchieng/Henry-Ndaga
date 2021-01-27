from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=20 , null=True,help_text="Name of sender")
    email = models.EmailField(max_length=50 , null=True,)
    subject = models.CharField(max_length=100 , null=True,)
    message = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.name


    


