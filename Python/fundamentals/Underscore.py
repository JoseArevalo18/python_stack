class Underscore:
    #MAP
    def map(self,iterable, callback):
        for i in range(len(iterable)):
            iterable[i] = callback(iterable[i])
        return iterable
        #FIND
    def find(self, iterable, callback):
        for i in range(len(iterable)):
            if callback(iterable[i]):
                return iterable[i]
        #FILTER
    def filter(self, iterable, callback):
        lista = []
        for i in range(len(iterable)):
            if callback(iterable[i]):
                lista.append(iterable[i])
        return lista
        #REJECT
    def reject(self, iterable, callback):
        for i in range(len(iterable)-1,0,-1):
            if callback(iterable[i]):
                iterable.pop(i)
        return iterable

_ = Underscore() # sí, estamos configurando una instancia a una variable que es un guión bajo

doble = _.map([1,2,3,4], lambda num: num*2) #debe retornar [2,4,6,8]
print(doble)
busqueda = _.find([1,2,3,4,5,6], lambda x: x>4) #debe retornar el primer valor que es mayor que 4
print(busqueda)
pares = _.filter([1,2,3,4,5,6], lambda x:x%2==0) #debe retornar [2,4,6]
print(pares)
impares = _.reject([1,2,3,4,5,6], lambda x:x%2==0) #debe retornar [1,3,5] 
print(impares)