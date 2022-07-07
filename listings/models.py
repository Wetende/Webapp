from cgi import print_exception
from ctypes import addressof
from email.mime import image
from turtle import title
from django.db import models

# Create your models here.
class Listing(models.Model):
    title = models.CharField(max_length=150, default='property')
    price = models.IntegerField(default='0')
    num_bedrooms = models.IntegerField(default='0')
    num_bathrooms = models.IntegerField(default='0')
    square_footage = models.IntegerField(default='0')
    address = models.CharField(max_length=100, default='city')
#image 
def __str__(self):
    return self.