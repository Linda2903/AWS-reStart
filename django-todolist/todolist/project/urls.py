from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns=[
    path("", views.handle_projects, name="handle_projects"),
]