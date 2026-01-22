from django.db import models
import uuid
from project.models import Project

# Create your models here.

class Task(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=200)
    project=models.ForeignKey(Project, on_delete=models.CASCADE, related_name="task", null=True, blank=True)
