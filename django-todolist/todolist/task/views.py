from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from django.db import IntegrityError, OperationalError
import json
from project.models import Project
from task.models import Task
from tag.models import Tag

@csrf_exempt
@require_POST
def create_task(request):
    try:
        data = json.loads(request.body)
        
        # Verifica che il progetto esista
        project = Project.objects.get(id=data['project_id'])
        
        task = Task.objects.create(
            title=data['title'],
            project=project
        )

        if 'tag_ids' in data:
            tags=Tag.objects.filter(id__in=data['tag_ids'])
            task.tags.set(tags)

        
        return JsonResponse({
            'id': task.id,
            'title': task.title,
            'is_complete': task.is_complete,
            'project_id': task.project.id,
            'tags': task.tags
        }, status=201)
    
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON non valido'}, status=400)
    
    except KeyError as e:
        return JsonResponse({'error': f'Campo mancante: {e}'}, status=400)
    
    except Project.DoesNotExist:
        return JsonResponse({'error': 'Progetto non trovato'}, status=404)
    
    except IntegrityError:
        return JsonResponse({'error': 'Task già esistente'}, status=409)

@require_GET
def get_task(request, project_id):
    try:
        # 1. Usa filter() invece di get() - un progetto può avere più task
        # 2. Usa values() per serializzare
        tasks = list(Task.objects.filter(project_id=project_id).values())
        
        return JsonResponse(tasks, safe=False, status=200)
    
    except OperationalError:
        return JsonResponse({'error': 'Database non disponibile'}, status=503)
    

@csrf_exempt
@require_POST
def add_tag(request):
    try:
        data=json.loads(request.body)
        tag= Tag.objects.get(id=data['tag_id'])
        task=Task.objects.get(id=data['task_id'])

        task.tags.add(tag)
        return JsonResponse({
                'message': "Tag_aggiunto",
                'task_id': task.id,
                'tag': list[task.tags.name,task.tags.id]
            }, status=201)
    
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON non valido'}, status=400)
    
    except KeyError as e:
        return JsonResponse({'error': f'Campo mancante: {e}'}, status=400)
    
    except Project.DoesNotExist:
        return JsonResponse({'error': 'tag non trovato'}, status=404)
    
    except IntegrityError:
        return JsonResponse({'error': 'Task già esistente'}, status=409)