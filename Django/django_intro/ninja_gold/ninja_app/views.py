from django.shortcuts import render, redirect
from datetime import datetime
import random

def index(request):
    if 'sum_oro' not in request.session or 'activities' not in request.session:
        request.session['sum_oro'] = 0
        request.session['activities'] = ""
    return render(request, 'index.html')

def dinero(request):
    if request.method == "POST":
        if request.POST['tipo_oro'] == 'farm':
            your_gold = random.randint(10, 21)
            request.session['activities']  += '\nGanando ' + str(your_gold) + ' Oro de la Granja! ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')' 
        elif request.POST['tipo_oro'] == 'cave':
            your_gold = random.randint(5, 11)
            request.session['activities'] += '\nGanando ' + str(your_gold) + ' Oro de la Caverna! ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')'
        elif request.POST['tipo_oro'] == 'house':
            your_gold = random.randint(2,6)
            request.session['activities'] += '\nGanando ' + str(your_gold) + ' Oro de la Casa ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')'
        elif request.POST['tipo_oro'] == 'casino':
            your_gold = random.randint(-50, 51)
            if your_gold >= 0:
                request.session['activities'] += '\nEntró en un Casino y ganó ' + str(your_gold) +' !!ORO!! ' + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')'
            else:
                request.session['activities'] += '\nEntró en un Casino y perdió ' + str(your_gold) + ' !!ORO!!... Diablos! ' + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')'
        request.session['sum_oro'] += your_gold
    

    return render(request,"index.html")

def reset(request):
    request.session.clear()
    return redirect("/")