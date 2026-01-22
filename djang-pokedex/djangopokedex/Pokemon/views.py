from django.db import IntegrityError, OperationalError
from django.shortcuts import render
from .models import Pokemon
from django.http import JsonResponse
import json
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt  #comunica al server che riceverà chiamate da API differenti (Con questo comando il server ha il via libera a eseguire tutte le richieste)
@require_POST   #decoratore
def add_pokemon(request):
    try:
        data = json.loads(request.body)
        pokemon = Pokemon.objects.create(name=data['name'], pokedex_id=data['pokedex_id'])
        return JsonResponse({'id': str(pokemon.id), 'name': pokemon.name, 'pokedex_id': pokemon.pokedex_id}, status=201)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON non valido'}, status=400)
    except KeyError as e:
        return JsonResponse({'error': f'Campo mancante: {e}'}, status=400)
    except IntegrityError:
        return JsonResponse({'error': 'Pokemon con questo nome già esistente'}, status=400)
    except OperationalError:
        return JsonResponse({'error': 'Database non disponibile'}, status=503)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
        
@require_GET
def get_pokemon_list(request):
    try:
        pokemon_list=list(Pokemon.objects.all().values())
        return JsonResponse(pokemon_list,safe=False)
    except OperationalError:
        return JsonResponse({'error':'Database non disponibile'}, status=503)
    except Exception as e:
        return JsonResponse({'error': {e}}, status=500)

@csrf_exempt    
@require_http_methods(['DELETE'])
def delete_pokemon(request, id):
    try:
        pokemon=Pokemon.objects.get(id=id) #preleva il pokemon
        pokemon.delete()   #elimina il pokemon
        return JsonResponse({'message':'Pokemon elminato'}, status=200)
    except Pokemon.DoesNotExist:
        return JsonResponse({'error':'Pokemon non trovato'}, status=400)

@csrf_exempt  
@require_http_methods(['PATCH'])
def update_patch_pokemon(request,id):
    try:
        data=json.loads(request.body)
        pokemon=Pokemon.objects.get(id=id)

        if 'name' in data:
            pokemon.name=data['name']
        if 'pokedex_id' in data:
            pokemon.pokedex_id=data['pokedex_id']

        pokemon.save()

        return JsonResponse({
            'id': pokemon.id,
            'name': pokemon.name,
            'pokedex_id':pokemon.pokedex_id
        }, status=200)
    
    except Pokemon.DoesNotExist:
        return JsonResponse({'error':'Pokemon non trovato'}, status=400)
    
    except json.JSONDecodeError:
        return JsonResponse({'error':'Json non trovato'}, status=400)
    

@csrf_exempt  
@require_http_methods(['PUT'])
def update_put_pokemon(request,id):
    try:
        data=json.loads(request.body)
        pokemon=Pokemon.objects.get(id=id)
        pokemon.name=data['name']
        pokemon.pokedex_id=data['pokedex_id']

        pokemon.save()

        return JsonResponse({
            'id': pokemon.id,
            'name': pokemon.name,
            'pokedex_id':pokemon.pokedex_id
        }, status=200)
    
    except Pokemon.DoesNotExist:
        return JsonResponse({'error':'Pokemon non trovato'}, status=400)
    
    except json.JSONDecodeError:
        return JsonResponse({'error':'Json non trovato'}, status=400)