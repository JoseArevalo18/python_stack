from django.shortcuts import HttpResponse

def nuevo(request):
    return HttpResponse("marca la posicion para que los usuarios creen un nuevo registro")

def loginf(request):
    return HttpResponse("marca la posicion para que los usuarios inicien sesion")

def index(request):
    return HttpResponse("marca de posicion para luego mostrar toda la lista de usuarios")
