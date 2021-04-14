from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "user"
        verbose_name_plural ="users"