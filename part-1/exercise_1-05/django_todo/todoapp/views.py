from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello there, I am a simple html-page!")
