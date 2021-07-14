from django.shortcuts import redirect, render
from .models import Course,Description
from django.contrib import messages

def index(request):
    context = {
                'all_courses' : Course.objects.all(),
                'all_descriptions' : Course.objects.all()
            }
    return render(request,'index.html',context)

def addCourse(request):
    errors = Course.objects.form_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/')
    else:  
        if request.method == "POST":
            new_course = Course.objects.create(name = request.POST['name'],)
            Description.objects.create(description = request.POST['description'],course = new_course)
        return redirect('/')

def  deleteCourse(request,number):
    if request.method == "POST":
        if request.POST['confirm'] == "No":
            return redirect('/')
        else:
            del_course = Course.objects.get(id=number)
            del_course.delete()
            return redirect('/')
    context = {
        'del_course' : Course.objects.get(id=number)
    }
    return render(request,'destroy.html',context)