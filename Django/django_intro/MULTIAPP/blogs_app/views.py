from django.http.response import JsonResponse
from django.shortcuts import redirect,HttpResponse
from django.http import JsonResponse

def root(request):
    return redirect("/blogs")

def index(request):
    return HttpResponse("PLACEHOLDER MOSTRARA UNA LISTAD DE TODOS LOS BLOGS")

def new(request):
    return HttpResponse("PLACEHOLDER MOSTRARA UN NUEVO FORMULARIO")

def create(request):
    return HttpResponse("PLACEHOLDER MOSTRARA UN NUEVO FORMULARIO PARA CREAR UN BLOG")

def show(request,number):
    return HttpResponse(f"PLACEHOLDER NOS MOSTRARA EL BLOG NUMERO: {number}")

def edit(request,number):
    return HttpResponse(f"PLACEHOLDER MOSTRARA PARA EDITAR EL BLOG NUMERO: {number}")
    
def destroy(request,number):
    return redirect("/blogs")

def jres(request):
    return JsonResponse({' UN TITULO ':'!!ESTO ES UN JSON!!'})