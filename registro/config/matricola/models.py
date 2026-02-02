from django.db import models
import uuid
from django.contrib.auth.models import User as AuthUser

# Create your models here.

class Matricola(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    matricola=models.TextField()
    user=models.OneToOneField(AuthUser, on_delete=models.CASCADE, related_name="matricola")
