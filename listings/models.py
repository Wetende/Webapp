from cgi import print_exception
from ctypes import addressof
from email.mime import image
from turtle import title
from django.db import models

# Create your models here.
class Listing(models.Model):
    pass
title = models.CharField(max_length=150)
price = models.IntegerField()
num_bedrooms = models.IntegerField()
num_bathrooms = models.IntegerField()
square_footage = models.IntegerField()
address = models.CharField(max_length=100)
#image 