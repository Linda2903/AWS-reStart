from django.db import models
from django.contrib.auth.models import AbstractUser
from matricola.models import Matricola
# Create your models here.

class User(AbstractUser):
    bio=models.textField(blank=True)
    lindedin_url=models.URLField(blank=True)

    def __str__(self):
        return self.username