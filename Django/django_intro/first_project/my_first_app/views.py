from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse("esto es equivalente @app.route('/')!")