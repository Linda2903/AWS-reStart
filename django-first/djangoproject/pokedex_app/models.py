from django.db import models

# Create your models here.
class Pokemon(models.Model):
    nome=models.CharField(max_length=100)
    tipo=models.CharField(max_length=200)
    livello=models.IntegerField(default=1)
    punti_salute=models.IntegerField()
    descrizione=models.TextField(blank=True, null=True)
    
    def __str_(self):
        return self.nome