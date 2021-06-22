from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse('Placeholder para mostrar todas las encuestas creadas')

def new(request):
    return HttpResponse('Placeholder para que los usuarios agreguen una nueva encuesta')