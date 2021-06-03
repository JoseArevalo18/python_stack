import random

def randInt(min=0, max=125):
    if min > max:
        return "Valor minimo no deberia ser mayor al maximo!"
    elif max < 0:
        return "Valor maximo no puede ser menor que 0!"
    else:
        top = max-min
        num = random.random() * top + min
        return round(num)


print(randInt())
print(randInt(max=1))
print(randInt(min=20))
print(randInt(min=-10, max=-1))