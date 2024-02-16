from django.db import models
from loginAndSignup.models import CustomUser

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.CharField(max_length = 2000)
    price = models.DecimalField(blank = False, decimal_places = 2, max_digits=10)
    images = models.ImageField(upload_to='UserPost/')
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)
    likes = models.IntegerField(default = 0)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
