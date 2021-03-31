from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=50)

    class Meta:
        verbose_name = "user"
        verbose_name_plural ="user"