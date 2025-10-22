from django.urls import path, include
from . views import home, actividades, exit, register

urlpatterns = [
    path('', home, name="home"),
    path('actividades/', actividades, name="actividades"),
    path('logout/', exit, name='exit'),
    path('register/', register, name='register'),
]