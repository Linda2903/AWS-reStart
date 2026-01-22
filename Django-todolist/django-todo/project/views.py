from django.db import IntegrityError, OperationalError
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST, require_http_methods

import json
from .models import Project


# Create your views here.
@csrf_exempt 
@require_POST
def add_project(request):
    try:
        data=json.loads(request.body)
        progetto=Project.objects.create(
            name=data['name']
        )
        return JsonResponse({'id':progetto.id,'name':progetto.name}, status=201)
    
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON non valido'}, status=400)
    
    except KeyError as e:
        return JsonResponse({'error': f'Campo mancante: {e}'}, status=400)
    
    except (ValueError, TypeError):
        return JsonResponse({'error': 'Tipo di dato non valido'}, status=400)
    
    except IntegrityError:
        return JsonResponse({'error': 'Progetto già esistente'}, status=409)
    
    except OperationalError:
        return JsonResponse({'error': 'Database non disponibile'}, status=503)
    
    except Exception as e:
        return JsonResponse({'error': 'Errore interno del server'}, status=500)
    
@csrf_exempt
@require_GET
def get_project_list(request):
    try:
        project_list = list(Project.objects.all().values())
        return JsonResponse(project_list, safe=False)
    
    except OperationalError:
        # Problemi di connessione al database
        return JsonResponse({'error': 'Database non disponibile'}, status=503)
    
    except Exception as e:
        # Errore generico imprevisto
        return JsonResponse({'error': str(e)}, status=500)
    


@csrf_exempt
@require_http_methods(['DELETE'])
def delete_project(request, id):
    try:
        progetto = Project.objects.get(id=id)
        progetto.delete()
        return JsonResponse({'message': 'Progetto eliminato'}, status=200)
    except Project.DoesNotExist:
        return JsonResponse({'error': 'Progetto non trovato'}, status=404)
    
    
@csrf_exempt
@require_http_methods(['PATCH'])
def update_patch_project(request, id):
    try:
        data = json.loads(request.body)
        progetto = Project.objects.get(id=id)
        
        # Aggiorna solo i campi presenti nel body
        if 'name' in data:
            progetto.name = data['name']
        
        progetto.save()
        
        return JsonResponse({
            'id': progetto.id,
            'name': progetto.name,
        }, status=200)
    
    except Project.DoesNotExist:
        return JsonResponse({'error': 'Progeto non trovato'}, status=404)
    
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON non valido'}, status=400)

    


