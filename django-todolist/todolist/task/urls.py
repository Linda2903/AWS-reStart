from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns=[
    path("create", views.create_task, name="create_task"),
    path("add_tag",views.add_tag ,name="add_tag"),
    path('<str:project_id>', views.get_task, name="get_task"),
]