from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,JsonResponse

def index(request):
    return HttpResponse("Hello. You're at the project index.")

user_data= {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
      "street": "Kulas Light",
      "suite": "Apt. 556",
      "city": "Gwenborough",
      "zipcode": "92998-3874",
      "geo": {
        "lat": "-37.3159",
        "lng": "81.1496"
      }
    }
    }

def pippo(request):
    return HttpResponse("Ciao, sono Pippo!")

def user(request):
    return JsonResponse(user_data)