from django.urls import path
from app import views

urlpatterns = [
    path('response.task_list', views.task_list),
    path('complete_task', views.complete_task),
    path('sample', views.sample),
    path('test', views.test)
]