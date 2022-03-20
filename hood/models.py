from multiprocessing import managers
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class hood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    description = models.TextField()
    chairman_name = models.CharField(max_length=100, blank=True)
    chairman_number = models.CharField(max_length=20, blank=True)
    chairman_email = models.EmailField(blank=True)
    dispensary_name = models.CharField(max_length=100, blank=True)
    dispensary_number = models.CharField(max_length=20, blank=True)
    dispensary_email = models.EmailField(blank=True)
    police_name = models.CharField(max_length=100, blank=True)
    police_number = models.CharField(max_length=20, blank=True)
    police_email = models.EmailField(blank=True)
    hood_pic =models.ImageField(upload_to='images/')

    
