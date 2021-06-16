from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse("ESTE ES MI PROYECTO DJANGO @app.route('/')!")