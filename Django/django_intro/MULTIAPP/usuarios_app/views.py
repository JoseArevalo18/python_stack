from django.shortcuts import HttpResponse

def nuevo(request):
    return HttpResponse("MARCA LA POSICION PARA QUE LOS USUARIOS CREEN UN NUEVO REGISTRO")

def loginf(request):
    return HttpResponse("MARCA LA POSICION PARA QUE LOS USUARIOS INICIEN SESION")

def index(request):
    return HttpResponse("MARCA LA POSICION PARA QUE LUEGO MUESTRE TODA LA LISTA DE USUARIOS")
