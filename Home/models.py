from django.db import models

# Create your models here.
class Home(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=150)

    def __str__(self):
        return self.summary