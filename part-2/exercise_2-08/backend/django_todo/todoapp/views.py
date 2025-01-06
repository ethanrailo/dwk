from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from . import utils
from .models import Todo

@csrf_exempt
def todos(request):
    if request.method == 'POST':
        try:
            todo_text = request.POST["todo_text"]
            t = Todo(todo_text=todo_text)
            t.save()
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