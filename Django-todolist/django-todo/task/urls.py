from . import views
from django.urls import path

urlpatterns=[
    path("add/",views.add_task ,name="add_task"),
    path("list/",views.get_task_list ,name="task_list"),
    path("delete/<str:id>",views.delete_task ,name="delete_task"),
    path("update/patch/<str:id>", views.update_patch_task, name="update_patch_task"),

]