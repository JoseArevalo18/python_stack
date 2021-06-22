from django.shortcuts import HttpResponse

def perrito(request):
    return HttpResponse('Placeholder para mostrar todas las encuestas creadas')

def index(request):
    return HttpResponse('Placeholder para que los usuarios agreguen una nueva encuesta')


