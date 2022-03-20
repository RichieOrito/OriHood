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



class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile') 
    house = models.CharField(max_length=50)
    phase = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True)
    profile_picture =models.ImageField(upload_to='images/')
    hood = models.ForeignKey(hood,on_delete=models.SET_NULL, null=True,related_name='neighbors',blank=True)



    class Business(models.Model):
        name=models.CharField(max_length=50)
        phone = models.CharField(max_length=50)
        start_day = models.CharField(max_length=50)
        end_day = models.CharField(max_length=50)
        open_time = models.CharField(max_length=50)
        close_time = models.CharField(max_length=50)
        business_image = models.ImageField(upload_to='images/')

        user=models.ForeignKey(Profile, on_delete=models.CASCADE) 
        neighborhood = models.ForeignKey(hood, on_delete=models.CASCADE)


    class PostType(models.Model):
        name = models.CharField(max_length=50)

        def __str__(self):
            return self.name

    class Post(models.Model):
        title = models.CharField(max_length=120, null=True)
        post = models.TextField()
        date = models.DateTimeField(auto_now_add=True)

        type = models.ForeignKey(PostType, on_delete=models.CASCADE, related_name='posts')
        user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
        hood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name='posts')


