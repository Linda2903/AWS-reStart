from . import views
from django.urls import path

urlpatterns=[
    path("add/",views.add_project ,name="add_project"),
    path("list/",views.get_project_list ,name="project_list"),
    path("delete/<str:id>",views.delete_project ,name="delete_project"),
    path("update/patch/<str:id>", views.update_patch_project, name="update_patch_project"),

]