from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from django.http.response import HttpResponse

def root(request):
    return redirect('random_word/')

def index(request):
    rnd_word = get_random_string(length=14)
    #contador = request.POST['csrfmiddlewaretoken']
    #request.session['count'] = 1
    context = {
        'rndWord': rnd_word,
        #'counter': 1,
    }
    if 'count' not in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 1
    return render(request, 'index.html', context)

def reset(request):
    request.session.clear()
    return redirect('/') 

############################################
    # if request.method == "POST":
    #     context['counter'] += 1
    #print(request.POST)
    #print(request.POST['csrfmiddlewaretoken'])