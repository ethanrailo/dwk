from django.urls import path

from . import views

urlpatterns = [
    path("", views.todos, name="todos"),
    path("quit", views.terminate_server, name="quit"), 
]