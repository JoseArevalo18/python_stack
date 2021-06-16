from django.http.response import JsonResponse
from django.shortcuts import redirect, render, HttpResponse
from django.http import JsonResponse

def root(request):
    return redirect('/')

def index(request):
    return HttpResponse("marcador de posición para luego mostrar una lista de todos los blogs")

def new(request):
    return HttpResponse("marcador de posición para mostrar un nuevo formulario para crear un nuevo blog")

def create(request):
    return redirect("/blogs/")

def show(request,number):
    return HttpResponse(f"marcardor de posicion para mostrar el blog numero: {number}")

def edit(request,number):
    return HttpResponse(f"marcador de posicion para editar el blog {number}")
    
def destroy(request,number):
    return redirect("/blogs")

def jres(request):
    return JsonResponse({'Titulo':'Un Json!!'})