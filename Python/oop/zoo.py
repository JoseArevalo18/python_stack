class Zoo:
    def __init__(self, zoo_nombre):
        self.animals = []
        self.nombre = zoo_nombre
    #AÑADE LA CLASE LEON CON EL NOMBRE,EDAD,FELICIDAD, HABITAD
    def add_lion(self, nombre,edad,n_salud,n_felicidad,habitat):
        self.animals.append( Leon(nombre,edad,n_salud,n_felicidad,habitat) )
        return self
    #AÑADE LA CLASE TIGRE CON EL NOMBRE,EDAD,FELICIDAD, HABITAD
    def add_tiger(self,  nombre,edad,n_salud,n_felicidad,habitat):
        self.animals.append( Tigre(nombre,edad,n_salud,n_felicidad,habitat) )
        return self
    #MOSTRARA LA INFORMACION O EL NOMBRE DEL ZOOLOGICO
    def print_all_info(self):
        print("-"*30, self.nombre, "-"*30)
        for animal in self.animals:
            animal.display_info()

class Animal(Zoo):
    def __init__(self,nombre,edad,n_salud,n_felicidad):
        self.nombre = nombre
        self.edad = edad
        self.n_salud = n_salud
        self.n_felicidad = n_felicidad
    #INFORMACION DEL ANIMAL EL CUAL ENTRARA AL ZOOLOGICO
    def display_info(self):
        print("Nombre:",self.nombre,"- Salud:",self.n_salud,"- Felicidad:",self.n_felicidad)
        return self
    #AUMENTO DE SALUD Y FELICIDAD, ADICIONAL MOSTRARA QUE ANIMAS ESTA COMIENDO EN ESE MOMENTO
    def alimentacion(self):
        self.n_salud += 10
        self.n_felicidad += 10
        print("-"*30,self.nombre,"Esta Comiendo!!", "-"*30)
        return self

class Leon(Animal):
    def __init__(self, nombre, edad, n_salud, n_felicidad,habitat):
        super().__init__(nombre, edad, n_salud, n_felicidad)
        self.habitat = habitat

class Tigre(Animal):
    def __init__(self, nombre, edad, n_salud, n_felicidad,habitat):
        super().__init__(nombre, edad, n_salud, n_felicidad)
        self.habitat = habitat

class Cebra(Animal):
    def __init__(self, nombre, edad, n_salud, n_felicidad,habitat):
        super().__init__(nombre, edad, n_salud, n_felicidad)
        self.habitat = habitat
#ANIMALES LOS CUALES VAN A ENTRAR AL ZOOLOGICO
Mufaza = Leon("Mufaza",25,80,50,"Savana")
Tigeer = Tigre("Tigeer",20,80,50,"Selva")
Marti = Cebra("Marti",12,80,50,"Savana")

Mufaza.display_info()
Mufaza.alimentacion().display_info()

zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala",20,20,20,"Selva")
zoo1.add_lion("Simba",20,20,20,"Selva")
zoo1.add_tiger("Rajah",20,20,20,"Selva")
zoo1.add_tiger("Shere Khan",20,20,20,"Selva")
zoo1.print_all_info()
zoo1.animals[0].alimentacion().display_info()