from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Pokemon

# Create your views here.

def pokemon_add(request):
    nuovo_pokemon=Pokemon.objects.create(nome="Bulbasaur", tipo="Erba",punti_salute=45,descrizione="Pokemon dalla velocità esorbitante e dall'ottima leggerezza.")
    return HttpResponse(f"Pokemon {nuovo_pokemon.nome} aggiunto con successo!")

def pokemon_list(request):
    pokemons=Pokemon.objects.all()
    output = ", ".join([f"Nome:{p.nome}- ID:{p.pk}" for p in pokemons])
    return HttpResponse(f"Lista Pokémon nel database: {output}")

def pokemon_delete(request, pk):
#usiamo la Primary Key (pk) per trovare l'elemento esatto
    pokemon=get_object_or_404(Pokemon, pk=pk)
    nome_cancellato=pokemon.nome
    pokemon.delete()
    return HttpResponse(f"Il pokemon {nome_cancellato} (Id:{pk}) è stato cancellato.")


