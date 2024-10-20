from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class MyUser(AbstractUser):
    username = models.CharField(max_length=200, unique=True,)
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True)

    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
    ]
