# # 1 Actualiza los valores en diccionarios y listas
#1)Cambia el valor 10 en x a 15. Una vez que haya terminado, x ahora debería ser [[5,2,3], [15,8,9]].
x = [[5, 2, 3], [10, 8, 9]]

def cambiarX(x):
    x[1][0] = 15
    return x

print(cambiarX(x))
#2)Cambia el apellido del primer alumno de 'Jordan' a 'Bryant'
alumnos = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]

def cambiarStudents():
    alumnos[0]["last_name"] = "Bryant"
    return alumnos

print(cambiarStudents())
#3)En el directorio sports_directory, cambia 'Messi' a 'Andres'
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}

def cambiarDirectory():
    sports_directory['soccer'][0] = "Andres"
    return sports_directory

print(cambiarDirectory())
#4)Camba el valor 20 en z a 30
z = [{'x': 10, 'y': 20}]

def cambiarZ():
    z[0]['y'] = 30
    return z

print(cambiarZ())

# 2 Itera a través de una lista de diccionarios

alumnos = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary(students):
    for i in range(len(students)):
        print(f"first_name"+" - "+students[i]["first_name"] +
            ", last_name"+" - "+students[i]["last_name"])


iterateDictionary(alumnos)

# # 3 Obtén valores de una lista de diccionarios

alumnos = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary2(key_name, students):
    for i in range(len(students)):
        print(students[i][key_name])


iterateDictionary2("first_name", alumnos)
iterateDictionary2("last_name", alumnos)

# # 4 Itera a través de un diccionario con valores de listas

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(dojo):
    print(str(len(dojo["locations"]))+"LOCATIONS")
    for i in range(len(dojo["locations"])):
        print(dojo["locations"][i])
    print(str(len(dojo["instructors"]))+"INSTRUCTORS")
    for i in range(len(dojo["instructors"])):
        print(dojo["instructors"][i])


printInfo(dojo)
