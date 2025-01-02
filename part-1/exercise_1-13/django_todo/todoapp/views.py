from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . import utils
from .models import Todo

def index(request):
    todo_list = Todo.objects.all()
    context = {
        "todo_list": todo_list
    }
    return render(request, "todoapp/index.html", context)

def get_image(request):
    image_data = utils.fetch_image_file()
    return HttpResponse(image_data, content_type="image/jpeg")

def todos(request):
    if request.method == 'POST':
        try:
            todo_text = request.POST["todo_text"]
            t = Todo(todo_text=todo_text)
            t.save()
            return HttpResponseRedirect(reverse(index))
        except:
            pass

        return HttpResponse(text="error")

    return HttpResponse("GET not really implemented rn")

def terminate_server(request):
    if not utils.shutdown_if_in_container():
        return HttpResponse("Not shutting down, since not in container.")
    
    return HttpResponse("gunicorn / container shutting down, bye!")