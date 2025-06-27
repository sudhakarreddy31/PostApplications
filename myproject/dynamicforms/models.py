from django.db import models

# Create your models here.

class Catagory(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField()


    def __str__(self):
        return self.name
    
class InformationForm(models.Model):
    title = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    email = models.EmailField()
    dropdown = models.CharField(max_length=123)
    checkbox = models.CharField(max_length=123)
    radio_option = models.CharField(max_length=125)
    terms = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    















