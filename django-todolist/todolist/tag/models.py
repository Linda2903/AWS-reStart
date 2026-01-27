from django.db import models
import uuid

# Create your models here.
class Tag(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=50, unique=True)
    #description=models.CharField(max_lenght=200)

    class Meta:                   #serve ad assegnare un nome specifico alla tabella Project (Projects)
        db_table="tags"
