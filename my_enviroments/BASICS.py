nombre = "Jose"
apellido = "Arevalo"
edad= 21
print("MI Nombre es "+ nombre + "" + apellido)

print (f"Mi nombre es: {nombre} {apellido} y mi edad es {edad}")

if (edad < 19):
    print("Eres menor de edad")
    print("Espera unos años")
elif (edad< 66):
    print("Eres un viejo")
else:
    print("Estas ya mas viejo")
suma = 0
for i in range (0,11):
    print(f"Numero {i}")
    suma += i

print(f"Suma total:{suma}")

alumnos = ["Jose","Sergio","Marcelo","Sara","Juan","Salomon","Pedro"]
for al in alumnos:
    if( not al.startswith("S")):
        print(f"Alumno: {al}")
print("IMPRESION INVERSA")
for al in range(len (alumnos), -1,-1) :
    print(f"Alumno: {alumnos[al-1]}")
print()
print("DICCIONARIO")
dict = {"nombre": nombre , "apellido": apellido, "edad": edad }
print(dict)

for key in dict.keys():
    print(f"Llave: {key}")

for val in dict.values():
    print(f"Valor: {val}")

for key,val in dict.items():
    print(f"Llave: {key}, Valor: {val}")


count = 0
while(count<5):
    print("looping -", count)
    count += 1

def sumar(maximo):
    suma = 0
    for i in range(0,maximo+1):
        suma += i
    return suma
suma_total=sumar(10) 
print (f"Suma total de funcion: {suma_total}")
print (f"Suma total de funcion: {sumar(10)}")

class Persona():
    tipo = "Persona"
    def __init__(self):
        self.nombre= "Jose"
        self.apellido= apellido
        self.edad= edad
    def Hablar(self):
        print (f"Hola a todos, me llamo: {self.nombre} {self.apellido}")

persona= Persona()

print(persona.tipo)

print(persona.nombre)
print(persona.apellido)
print(persona.edad)

print(Hablar()) 