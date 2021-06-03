import random

def randInt(minimo=0, maximo=125):
    if minimo > maximo:
        return "Valor minimo no deberia ser mayor al maximo!"
    elif maximo < 0:
        return "Valor maximo no puede ser menor que 0!"
    else:
        top = maximo-minimo
        num = random.random() * top + minimo
        return round(num)


print(randInt())
print(randInt(maximo=1))
print(randInt(minimo=20))
print(randInt(minimo=-10, maximo=-1))