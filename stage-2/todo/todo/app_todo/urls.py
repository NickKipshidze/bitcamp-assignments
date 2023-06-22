from django.urls import path
from . import views

urlpatterns = [
    path("tasks/", views.TaskList.as_view(), name="task_list"),
    path("task/create/", views.TaskCreate.as_view(), name="task_create"),
    path("task/<int:id>/", views.TaskDetail.as_view(), name="task_detail"),
    path("task/<int:id>/update/", views.TaskUpdate.as_view(), name="task_update"),
    path("task/<int:id>/delete/", views.TaskDelete.as_view(), name="task_delete"),
]
