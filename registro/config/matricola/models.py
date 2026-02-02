from django.db import models
import uuid
from django.contrib.auth.models import User as AuthUser

# Create your models here.

class Matricola(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    matricola=models.TextField()
    user=models.OneToOneField(AuthUser, on_delete=models.CASCADE, related_name="matricola")

    def __str__(self):
        """
        Return a human-readable representation of the Matricola instance,
        including the matricola value and the associated user's username.
        """
        return f"{self.matricola} ({self.user.username})"
    class Meta:
        db_table = "matricolas"