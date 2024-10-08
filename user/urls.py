from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register

urlpatterns = [
    path('login/', LoginView.as_view(template_name="user/login.html"), name='login'),
    path('logout/', LogoutView.as_view(template_name="user/logout.html"), name='logout'),
    path('register/', register, name='register'),
]
