from django.db import models
from django.contrib.auth.models import AbstractUser

from mywebsite import settings

# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(unique = True)
    profile_photo = models.ImageField(blank=True,upload_to='images/')
    followers = models.IntegerField(default = 0)
    about = models.CharField(max_length = 300,blank = True)
    REQUIRED_FIELDS = ['email']


class Post(models.Model):    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(max_length = 2000)
    price = models.DecimalField(blank = False, decimal_places = 2, max_digits=10)
    images = models.ImageField(upload_to='UserPost/')
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)
    likes = models.IntegerField(default = 0)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
