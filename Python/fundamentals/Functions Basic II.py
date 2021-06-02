                                    #EJERCICIO 1
#crea una función que acepte un número como entrada. Devuelve una nueva lista que cuenta hacia atrás en uno, desde el número (como el elemento 0) hasta 0 (como el último elemento).
#Ejemplo: la cuenta regresiva (5) debería devolver [5,4,3,2,1,0]
for x in range(5,-1,-1):
    print(x)
                                    #EJERCICIO 2
#crea una función que recibirá una lista con dos números. Imprima el primer valor y devuelva el segundo.
#Ejemplo: print_and_return ([1,2]) debería imprimir 1 y devolver 2
def x():
    print(1)
    return 2
print(x())
                                    #EJERCICIO 3
#crea una función que acepta una lista y devuelve la suma del primer valor de la lista más la longitud de la lista.
#Ejemplo: first_plus_length ([1,2,3,4,5]) debería devolver 6 (primer valor: 1 + longitud: 5)
def first_plus_length(arr):
    x=arr[0]+ len(arr)
    return x
print(first_plus_length([1,2,3,4,5]))
                                    #EJERCICIO 4
#escribe una función que acepte una lista y crea una nueva lista que contenga solo los valores de la lista original que sean mayores que su segundo valor. Imprima cuántos valores son y luego devuelva la nueva lista. Si la lista tiene menos de 2 elementos, haga que la función devuelva False
#Ejemplo: values_greater_than_second ([5,2,3,2,1,4]) debería imprimir 3 y devolver [5,3,4]
#Ejemplo: values_greater_than_second ([3]) debería devolver False
def funcion(arr):
    listnueva=[]
    for i in range (0,len(arr),1):
        if len(arr)<2:
            return False
        elif arr[i]>arr[1]:
            listnueva.append(arr[i])
    return listnueva


print(funcion([5,2,3,2,1,4]))
print(funcion([3]))
                                    #EJERCICIO 5
#escribe una función que acepte dos enteros como parámetros: tamaño y valor. La función debe crear y devolver una lista cuya longitud es igual al tamaño dado y cuyos valores son todos los valores dados.
#Ejemplo: length_and_value (4,7) debería devolver [7,7,7,7]
#Ejemplo: length_and_value (6,2) debería devolver [2,2,2,2,2,2]
def valores(a,b):
    lis=[]
    for i in range (0,a+1,1):
        lis.append(b)
    return lis

print(valores(4,7))
print(valores(6,2))