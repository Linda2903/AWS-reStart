from django.db import models
from django.contrib.auth.models import User as AuthUser
import uuid
from project.models import Project

# Create your models here.
class Project_details(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    notes=models.CharField(max_length=200)
    #description=models.CharField(max_lenght=200)

    """
    Con questa istruzione definisco la relazione 1 a 1 tra ProjectDetails e Project
    """
    project= models.OneToOneField(
        Project, on_delete=models.CASCADE, related_name="project"
    )


    class Meta:                   #serve ad assegnare un nome specifico alla tabella Project (Projects)
        db_table="projects_details"
    
