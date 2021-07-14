from typing import ContextManager
from django.contrib import messages
from django.db.models.expressions import Value
from django.shortcuts import redirect, render
from .models import Show

def index(request):
    return render(request, 'index.html')

def addShow(request):
    errors = Show.objects.form_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/shows/new')
    else:
        new_show = Show.objects.create(
                title = request.POST['titleInput'],
                network = request.POST['networkInput'],
                release_date = request.POST['dateInput'],
                description = request.POST['descriptionInput'],
            )
        context = {
                'new_show' : new_show
            }
        return render(request, 'one_show.html',context)

def displayShow(request):
    context = {
        'all_shows' : Show.objects.all()
    }
    return render(request, 'shows.html',context)

def showInfo(request,number):
    new_show = Show.objects.get(id=number)
    context = {
        'new_show' : new_show
    }
    return render(request, 'one_show.html',context)

def editShow(request,number):
    if request.method == "POST":
        errors = Show.objects.form_validator(request.POST)
        if len(errors) > 0:
            edit_show = Show.objects.get(id=number)
            context = {
                    'new_show' : edit_show
            }
            for key, value in errors.items():
                messages.error(request,value)
            context['up_date']= str(context['new_show'].release_date)
            return render(request, 'edit_show.html',context)
        else:
            update_show = Show.objects.get(id=request.POST['show_id'])
            update_show.title = request.POST['titleInput']
            update_show.network = request.POST['networkInput']
            update_show.release_date = request.POST['dateInput']
            update_show.description = request.POST['descriptionInput']
            update_show.save()
            context = {
                'new_show' : update_show
            }
            return render(request, 'one_show.html',context)
    edit_show = Show.objects.get(id=number)
    context = {
        'new_show' : edit_show
    }
    context['up_date']= str(context['new_show'].release_date)
    return render(request, 'edit_show.html',context)

def delete_show(request,number):
    del_show = Show.objects.get(id=number)
    del_show.delete()
    return redirect('/shows/')

def showNetworks(request):
    context = {
        'all_net' :Show.objects.all()
    }
    return render(request, 'networks.html',context)