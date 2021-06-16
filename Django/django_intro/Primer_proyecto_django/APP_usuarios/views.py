from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponse
from django.http import JsonResponse

def newreg(request):
    return HttpResponse("marcador de posición para que los usuarios creen un nuevo registro de usuario")

def loginfunc(request):
    return HttpResponse("marcador de posición para que los usuarios inicien sesión")

def index(request):
    return HttpResponse("marcador de posición para luego mostrar toda la lista de usuarios")
