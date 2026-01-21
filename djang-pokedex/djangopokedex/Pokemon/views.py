from django.shortcuts import render
from .models import Pokemon
from django.http import JsonResponse
import json
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt  #comunica al server che riceverà chiamate da API differenti (Con questo comando il server ha il via libera a eseguire tutte le richieste)
@require_POST   #decoratore
def add_pokemon(request):
    data=json.loads(request.body)  #così prendiamo il body dalla request
    pokemon=Pokemon.objects.create(name=data['name'], pokedex_id=data['pokedex_id'])
    return JsonResponse({'id':pokemon.id, 'name': pokemon.name, 'pokedex_id': pokemon.pokedex_id},status=201)