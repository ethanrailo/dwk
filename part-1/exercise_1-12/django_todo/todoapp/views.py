from django.shortcuts import render
from django.http import HttpResponse
from . import utils

def index(request):
    context = {}
    return render(request, "todoapp/index.html", context)

def get_image(request):
    image_data = utils.fetch_image_file()
    return HttpResponse(image_data, content_type="image/jpeg")

def terminate_server(request):
    if not utils.shutdown_if_in_container():
        return HttpResponse("Not shutting down, since not in container.")
    
    return HttpResponse("gunicorn / container shutting down, bye!")