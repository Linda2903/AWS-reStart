from django.db import models
import uuid
from project.models import Project
from tag.models import Tag

# Create your models here.
class Task(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title=models.CharField(max_length=50, unique=True)
    is_complete=models.BooleanField(default=False)

    project= models.ForeignKey(Project, on_delete=models.CASCADE, related_name="projects")  #il related name deve essere il nome della tabella

    tags=models.ManyToManyField(Tag, related_name="tasks",blank=True)

    class Meta:                   #serve ad assegnare un nome specifico alla tabella Project (Projects)
        db_table="tasks"


    """
    Specifichiamo le relazione molti a molti tra task e tag nel modello
    dei task perchè sono i task che usano i tag.
    """