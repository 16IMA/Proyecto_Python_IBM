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
        
    def eliminarProducto(self, nombre_producto):
         for producto in self.productos:
              if producto.nombre == nombre_producto:
                   self.productos.remove(producto)
                   return print("Producto eliminado")
              else:
                return print("Producto inexistente")

i=0
while i == 0:
    print("— Menú de Inventario —")
    print("1.Agregar producto")
    print("2.Actualizar producto")
    print("3.Eliminar producto")
    print("4.Mostrar inventario")
    print("5.Buscar producto")
    print("6.Salir")
    option= int(input("Seleccionar una opción: "))

    inventario = Inventario()  
    if option==1:
        nombre = input("Ingrese el nombre del producto: ")  
        categoria = input("Ingrese la categoría del producto: ")
        precio = int(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        nuevo_producto = Producto(nombre, categoria, precio, cantidad)
        inventario.agregarProducto(nuevo_producto)
    print("Producto agregado correctamente.")
    
    elif option==3:
       input("Ingrese el nombre del producto que desea eliminar: ")
       
       print(lista_nombre_seleccionado)
       print("¿Está seguro de eliminar este producto? (S/N): ")
       confirmacion=input()
            if confirmacion.upper()=="S":
                    del(lista_producto)
                    print("Producto eliminado correctamente.")
            else:
                    print("Eliminación cancelada")


    