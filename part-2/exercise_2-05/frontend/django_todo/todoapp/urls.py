from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("random_image", views.get_image, name="get_image"),
    path("quit", views.terminate_server, name="quit"), 
]