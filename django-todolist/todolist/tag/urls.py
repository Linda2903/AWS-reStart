from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns=[
    path('create', views.create_tag, name="create_tag")
]
