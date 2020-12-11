from django.urls import path
from app import views

urlpatterns = [
    path('complete.task', views.task_complete),
    path('check.task', views.task_check),
    path('check.task_list', views.tasklist_check),
    path('check.task_detail', views.taskdetail_check)
]
