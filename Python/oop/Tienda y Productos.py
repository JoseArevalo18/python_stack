class tienda:
    def __init__(self,nombre,productos):
        self.nombre = nombre
        self.productos = productos
    
    def add_product (self, new_product):
        self.productos.append(new_product)
        
        return self
    
    def sell_product (self, id):
        print("Se ha eliminado el producto: ", self.productos[id].nombre)
        self.productos.pop(id)
        return self
        
    def inflation(self, percent_increase):
        producto.update_price(percent_increase,True)
        return self
    
    def set_clearance(self, category,percent_discount):
        if producto.categoria == category:
            producto.update_price(percent_discount,False)
        else:
            print("No Existe Categoria!!")
        return self

class producto:
    def __init__(self,nombre,precio,categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
    
    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.precio += self.precio * percent_change
        elif is_increased == False:
            self.precio -= self.precio * percent_change

    def print_info (self):
        print(self.nombre, self.precio, self.categoria)

mitienda = tienda("SANTA MARIA",[])

prod1 = producto("QUESO",2.00,"Lacteos")
prod2 = producto("EMPANADAS",1.50,"Panaderia")
prod3 = producto("Pan",0.35,"Panaderia")

mitienda.add_product(prod1).add_product(prod2).add_product(prod3).sell_product(1).add_product(prod1).sell_product(2)