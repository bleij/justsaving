from django.urls import path
from .views import UpdateTask, delete_task

urlpatterns = [
    path('update/task/<int:pk>/', UpdateTask.as_view(), name='update_task'),
    path('delete/task/<int:pk>', delete_task, name='delete_task'),

]
