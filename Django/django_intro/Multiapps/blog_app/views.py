from django.shortcuts import HttpResponse, redirect

def root(request):
    return redirect('')

def index(request):
    return HttpResponse("Placeholder para mostrar una lista de todos los blogs")

def new(request):
    return HttpResponse("Placeholder para mostrar un nuevo formulario para crear un nuevo blog")

def create(request):
    return redirect('/blogs')

def show(request, number):
    return HttpResponse(f"Placeholder para mostrar el blog número {number}")

def edit(request, number):
    return HttpResponse(f'Placeholder para editar el blog {number}')

def destroy(request, number):
    return redirect('/blogs')