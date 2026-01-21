from django.urls import path
from . import views

urlpattern=[
    path("add",views.add_pokemon, name="add_pokemon"),
]