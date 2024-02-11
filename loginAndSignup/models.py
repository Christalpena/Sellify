from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(unique = True)
    profile_photo = models.ImageField(blank=True,upload_to='images/')
    REQUIRED_FIELDS = ['email']

    