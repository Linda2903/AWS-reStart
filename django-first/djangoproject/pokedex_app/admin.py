from django.contrib import admin
from .models import Pokemon

class PokemonAdmin(admin.ModelAdmin):
    # Questo ti permette di vedere l'ID nella tabella dell'area admin
    list_display = ('id', 'nome', 'tipo', 'livello')

admin.site.register(Pokemon, PokemonAdmin)

