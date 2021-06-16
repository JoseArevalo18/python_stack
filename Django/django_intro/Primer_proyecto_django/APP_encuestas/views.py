from django.http.response import JsonResponse
from django.shortcuts import redirect, render, HttpResponse
from django.http import JsonResponse

def root(request):
    return HttpResponse("marcador de posición para mostrar todas las encuestas creadas")

def index(request):
    return HttpResponse("marcador de posición para que los usuarios agreguen una nueva encuesta")