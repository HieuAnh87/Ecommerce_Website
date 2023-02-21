from django.db import models
from django.contrib.auth.models import AbstractUser  # custom model


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150)
    bio = models.TextField(max_length=500, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

