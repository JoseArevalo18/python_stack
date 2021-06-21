
from django.shortcuts import render, redirect
from time import gmtime, localtime, strftime

def root(request):
    return redirect('/time_display')

def index(request):
    return render(request, 'index.html')
    
def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime()),
        "localTime": strftime("%Y-%m-%d %H:%M %p", localtime())
    }
    return render(request,'index.html', context)