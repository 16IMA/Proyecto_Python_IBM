
class Producto():

# Declaración de atributos

    def __init__(self, nombre, categoria, precio, cantidad): 
        self.nombre= nombre 
        self.categoria= categoria
        self.precio= precio
        self.cantidad= cantidad


class Inventario():

# Declaración de metodos

    def __init__(self):
        self.productos = [] 

    def agregarProducto(self, producto):
        self.productos.append(producto)
        

