from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from . import utils
from .models import Todo

@csrf_exempt
def todos(request):
    if request.method == 'POST':
        try:
            print(f"POST request sent from {request.headers["Host"]}")
            todo_text = request.POST["todo_text"]

            if len(todo_text) > 140:
                print(f"Host {request.headers["Host"]} sent too long todo-text: {todo_text}. This will be automatically blocked (http 400) by Django, since the 140 char limit is set in the model.")
            else:
                print(f"Host {request.headers["Host"]} sent valid todo-text: {todo_text}.")

            t = Todo(todo_text=todo_text)
            t.save()
            print("New todo saved.")
            return JsonResponse({"status": "ok"})
        except Exception as error:
            print(error)
            return HttpResponseBadRequest()

    if request.method == 'GET':
        try:
            data = serializers.serialize('json', Todo.objects.all())
            return HttpResponse(data, content_type='application/json')
        except:
            return HttpResponse(text="error")

    return HttpResponse("Method not implemented.")

def terminate_server(request):
    if not utils.shutdown_if_in_container():
        return HttpResponse("Not shutting down, since not in container.")
    
    return HttpResponse("gunicorn / container shutting down, bye!")