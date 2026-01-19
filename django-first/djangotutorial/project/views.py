from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse

from .models import Project

def index(request):
    projects=Project.objects.all().values()
    print(projects)
    return JsonResponse(list(projects),safe=False)

def add_project(request):
    project=Project.objects.create(title="Nuovo progetto", is_available=True)
    return JsonResponse({'id':project.id, 'title':project.title, 'is_avialable':project.is_available})


