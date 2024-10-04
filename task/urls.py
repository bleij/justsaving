from django.urls import path
from .views import update_task, delete_task
from core.views import task_list_view

urlpatterns = [
    path('', task_list_view, name='task_list'),
    path('update/task/<int:pk>/', update_task, name='update_task'),
    path('delete/task/<int:pk>', delete_task, name='delete_task'),

]
