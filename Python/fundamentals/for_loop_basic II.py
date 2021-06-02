                        #EJERCICIO 1
    #TAMAÑO GRANDE
# Dada una lista, escriba una función que cambie todos los números positivos de la lista a "big".
# Ejemplo: biggie_size ([- 1, 3, 5, -5]) devuelve la misma lista, pero cuyos valores son ahora [-1, "big", "big", -5]

def cambio(arr):
    lis=[]
    for i in range(0,len(arr),1):
        if arr[i]>0:
            lis.append("big")
        else:
            lis.append(arr[i])
    return lis
print(cambio([-1,3,5,-5]))

                        #EJERCICIO 2
    #CONTAR POSITIVOS
# dada una lista de números, cree una función para reemplazar el último valor con el número de valores positivos. (Tenga en cuenta que cero no se considera un número positivo).
# Ejemplo: count_positives ([- 1,1,1,1]) cambia la lista original a [-1,1,1,3] y la devuelve
# Ejemplo: count_positives ([1,6, -4, -2, -7, -2]) cambia la lista a [1,6, -4, -2, -7,2] y la devuelve

def positivos(lista):
    contador=0
    for i in lista:
        if i>0:
            contador+=1
    lista[len(lista)-1]=contador
    return lista
print(positivos([-1,1,1,1]))
print(positivos([1,6,-4,-2,-7,-2]))

    
                        #EJERCICIO 3
    #SUMA TOTAL
#crea una función que toma una lista y devuelve la suma de todos los valores de la matriz.
# Ejemplo: sum_total ([1,2,3,4]) debería devolver 10
# Ejemplo: sum_total ([6,3, -2]) debería devolver 7

def sumalista(listaNumeros):
    laSuma = 0
    for i in range(0,len(listaNumeros),1): #o tambien for i in listaNumeros:
        laSuma = laSuma + listaNumeros[i]  #laSuma = laSuma + i
    return laSuma

print(sumalista([1,2,3,4]))
print(sumalista([6,3,-2]))

                        #EJERCICIO 4
    #PROMEDIO
#crea una función que toma una lista y devuelve el promedio de todos los valores.
# Ejemplo: el promedio ([1,2,3,4]) debería devolver 2.5

def promedio(numeros):
    suma=0
    for i in range(0,len(numeros),1):
        suma=suma + numeros[i]
    return suma/len(numeros)
print(promedio([1,2,3,4]))

                        #EJERCICIO 5
    #LONGITUD
#crea una función que toma una lista y devuelve la longitud de la lista.
# Ejemplo: la longitud ([37,2,1, -9]) debería devolver 4
# Ejemplo: longitud ([]) debería devolver 0

def longitud(arr):
    return len(arr)
print(longitud([37,2,1,-9]))
print(longitud([]))

                        #EJERCICIO 6
    #MINIMO
#crea una función que tome una lista de números y devuelva el valor mínimo en la lista. Si la lista está vacía, haga que la función devuelva False.
# Ejemplo: mínimo ([37,2,1, -9]) debería devolver -9
# Ejemplo: mínimo ([]) debería devolver False

def minimo(arr):
    comparacion=0
    if len(arr)==0:
        return False
    else:
        for i in range (0,len(arr),1):
            arr[i]<comparacion
            comparacion=arr[i]
        return comparacion
print(minimo([37,2,1,-9]))
print(minimo([]))

                        #EJERCICIO 7
    #MAXIMO
#crea una función que toma una lista y devuelve el valor máximo en la matriz. Si la lista está vacía, haga que la función devuelva False.
# Ejemplo: máximo ([37,2,1, -9]) debería devolver 37
# Ejemplo: máximo ([]) debería devolver False

def Maximo(lista):
    grande=0
    if len(lista)==0:
        return False
    for numero in lista:
        if numero>grande:
            grande=numero
    return grande

print(Maximo([37,2,1,-9]))
print(Maximo([]))

                        #EJERCICIO 8
    #ANALISIS FINAL
#crea una función que tome una lista y devuelva un diccionario que tenga la suma total, promedio, mínimo, máximo y longitud de la lista.
# Ejemplo: ultimate_analysis ([37,2,1, -9]) debería devolver {'totalTotal': 31, 'promedio': 7.75, 'mínimo': -9, 'máximo': 37, 'longitud': 4}

def final(lista):
    list=[]
    total=0
    promedio=0
    minimo=0
    maximo=0
    longitud=0
    for i in lista:
            #suma
            total=total+i
            #promedio
            promedio=total/len(lista)
            #minimo
            if i<minimo:
                minimo=i
            #maximo
            elif i>maximo:
                maximo=i
            #longitud
            longitud=len(lista)
    list.append(f"Totaltolal: {total}")
    list.append(f"Promedio: {promedio}")
    list.append(f"Minimo: {minimo}")
    list.append(f"Maximo: {maximo}")
    list.append(f"Longitud: {longitud}")
    
    return list
print(final([37,2,1,-9]))

                        #EJERCICIO 9
    #LISTA INVERSA
#crea una función que tome una lista y la devuelva con los valores invertidos. Haz esto sin crear una segunda lista. (Se sabe que este desafío aparece durante las entrevistas técnicas básicas).
# Ejemplo: reverse_list ([37,2,1, -9]) debería devolver [-9,1,2,37]

lista=[37,2,1,-9]
lista.reverse()
print(lista)
