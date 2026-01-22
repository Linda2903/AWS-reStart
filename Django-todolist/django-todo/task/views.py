from django.db import IntegrityError, OperationalError
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from project.models import Project

import json
from .models import Task

@csrf_exempt 
@require_POST
def add_task(request):
    try:
        data=json.loads(request.body)
        task=Task.objects.create(
            name=data['name'],
            project=data['project']
        )
        return JsonResponse({'id':task.id,'name':task.name, 'project':task.project}, status=201)
    
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON non valido'}, status=400)
    
    except KeyError as e:
        return JsonResponse({'error': f'Campo mancante: {e}'}, status=400)
    
    except (ValueError, TypeError):
        return JsonResponse({'error': 'Tipo di dato non valido'}, status=400)
    
    except IntegrityError:
        return JsonResponse({'error': 'Task già esistente'}, status=409)
    
    except OperationalError:
        return JsonResponse({'error': 'Database non disponibile'}, status=503)
    
    except Exception as e:
        return JsonResponse({'error': 'Errore interno del server'}, status=500)
    
   
@csrf_exempt
@require_GET
def get_task_list(request):
    try:
        task_list = list(Task.objects.all().values())
        return JsonResponse(task_list, safe=False)
    
    except OperationalError:
        # Problemi di connessione al database
        return JsonResponse({'error': 'Database non disponibile'}, status=503)
    
    except Exception as e:
        # Errore generico imprevisto
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
@require_http_methods(['DELETE'])
def delete_task(request, id):
    try:
        task = Task.objects.get(id=id)
        task.delete()
        return JsonResponse({'message': 'Progetto eliminato'}, status=200)
    except Task.DoesNotExist:
        return JsonResponse({'error': 'Progetto non trovato'}, status=404)

 
    
@csrf_exempt
@require_http_methods(['PATCH'])
def update_patch_task(request, id):
    try:
        data = json.loads(request.body)
        task = Task.objects.get(id=id)
        
        # Aggiorna solo i campi presenti nel body
        if 'name' in data:
            Task.name = data['name']
        
        task.save()
        
        return JsonResponse({
            'id': task.id,
            'name': task.name,
            'project':task.project
        }, status=200)
    
    except Task.DoesNotExist:
        return JsonResponse({'error': 'Progeto non trovato'}, status=404)
    
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON non valido'}, status=400)

    



    

