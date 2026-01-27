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
def create_tag(request):
    try:
        data = json.loads(request.body)
        
        """  Verifica che il progetto esista
            project = Project.objects.get(id=data['project_id']) """
        
        tag = Tag.objects.create(
            name=data['name']
        )

        return JsonResponse({
            'id': tag.id,
            'name': tag.name
        }, status=201)
    
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON non valido'}, status=400)
    
    except KeyError as e:
        return JsonResponse({'error': f'Campo mancante: {e}'}, status=400)
    
    except IntegrityError:
        return JsonResponse({'error': 'Tag già esistente'}, status=409)

@csrf_exempt
@require_GET
def get_tags(request):
    try:
        tag_list=list(Task.objects.all().values())
        return JsonResponse(tag_list,safe=False,status=200)
    except OperationalError:
        return JsonResponse({'error': 'Database non risponibile'}, status=503)
    

@csrf_exempt
@require_GET
def get_tags_by_task_id(request,task_id):
    try:
        tag_list=list(Tag.objects.filter(tasks=task_id).values())
        return JsonResponse(tag_list,safe=False,status=200)
    except OperationalError:
        return JsonResponse({'error': 'Database non risponibile'}, status=503)