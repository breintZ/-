from django.contrib.auth.models import AbstractUser
from django.db import models

#Модель пользователя
class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
