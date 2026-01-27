from django.urls import path
from django.contrib import admin
from . import views

urlpatterns=[
    path("<str:id>", views.update_details_project, name="update_details_project")
]