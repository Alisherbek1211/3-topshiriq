from django.db import models
from django.contrib.auth.models import AbstractBaseUser 
# Create your models here.


class User(models.Model):
    image = models.ImageField(upload_to='user/')
    is_author = models.BooleanField(default=False)