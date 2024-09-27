from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register
from core.views import home, task_list

urlpatterns = [
    path('', home, name='home'),
    path('tasks/', task_list, name='task_list'),
    path('login/', LoginView.as_view(template_name="user/login.html"), name='login'),
    path('logout/', LogoutView.as_view(template_name="user/logout.html"), name='logout'),
    path('register/', register, name='register'),
]
