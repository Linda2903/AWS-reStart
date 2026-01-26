from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET,require_http_methods
import json
from django.db import transaction, IntegrityError
from project_details.models import Project_details

# Create your views here.
@csrf_exempt
@require_http_methods(['PATCH'])
def update_details_project(request,id):
    try:
        data=json.loads(request.body)
        projects_details=Project_details.objects.get(id=id)


        if data.get["notes"]:
            projects_details.notes=data['notes']
        projects_details.save()

        return JsonResponse({
            'id':projects_details.id,
            'notes':projects_details.notes
        }, status=200)


    except Project_details.DoesNotExist:
        return JsonResponse({'error':'Project_detail non trovato'}, status=404)
    
    except json.JSONDecodeError:
        return JsonResponse({'error':'Json non trovato'}, status=400)