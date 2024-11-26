class Producto():

# Declaración de atributos

    def __init__(self, nombre, categoria, precio, cantidad): 
        self.nombre= nombre.upper() 
        self.categoria= categoria.upper()
        self.precio= precio
        self.cantidad= cantidad


class Inventario():

# Declaración de metodos

#Iniciamos una lista 

    def __init__(self):
        self.productos = []

#Método agregar productos

    def agregarProducto(self, producto):
        for prod in self.productos:
            if prod.nombre == producto.nombre:
                print(f"Error: El producto '{producto.nombre}' ya existe en el inventario.")
                return  
        
        
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado correctamente.")

#Método eliminar productos

    def eliminarProducto(self, nombre_producto):
         for producto in self.productos:
              if producto.nombre == nombre_producto:
                    self.productos.remove(producto)
                    return print("Producto eliminado")
              else:
                    return print("Producto inexistente")
    
#Método actualizar productos

def actualizarProducto(self, nombre_producto, nuevo_precio, nueva_cantidad):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                print(f"Producto encontrado: {producto.nombre}")
                print("1. Actualizar precio")
                print("2. Actualizar cantidad")
                opcion = input("Seleccione qué desea actualizar: ")

                if opcion == "1":
                    try:
                        nuevo_precio = float(input(f"Ingrese el nuevo precio (actual: {producto.precio}): "))
                        producto.precio = nuevo_precio
                        print(f"Precio actualizado correctamente a {producto.precio}.")
                    except ValueError:
                        print("Error: Debe ingresar un valor numérico para el precio.")
                elif opcion == "2":
                    try:
                        nueva_cantidad = int(input(f"Ingrese la nueva cantidad (actual: {producto.cantidad}): "))
                        producto.cantidad = nueva_cantidad
                        print(f"Cantidad actualizada correctamente a {producto.cantidad}.")
                    except ValueError:
                        print("Error: Debe ingresar un valor numérico para la cantidad.")
                else:
                    print("Opción inválida.")
                return
        print(f"Producto '{nombre_producto}' no encontrado.")


#Método buscar productos

    def buscarProducto(self, nombre_producto):
        for producto in self.productos:
              if producto == nombre_producto:
                   print(
                    f"Nombre: {producto.nombre}, Categoría: {producto.categoria}, "
                    f"Precio: {producto.precio}, Cantidad: {producto.cantidad}"
                )
                return
        print(f"No se encontró un producto con el nombre '{nombre_producto}'.")

#Método mostrar Inventario
    
    def mostrarInventario(self):
         for producto in self.productos:
              print(f"Nombre del producto: {producto.nombre}, categoría: {producto.categoria}, precio: {producto.precio}, cantidad: {producto.cantidad}")


#Programa principal

inventario = Inventario()

while True:
    print("\n— Menú de Inventario —")
    print("1.Agregar producto")
    print("2.Actualizar producto")
    print("3.Eliminar producto")
    print("4.Mostrar inventario")
    print("5.Buscar producto")
    print("6.Salir")
    option= int(input("Seleccionar una opción: "))
      
    if option==1:
        print("\n- Agregar productos -")
        nombre = input("Ingrese el nombre del producto: (o escriba 'salir' para finalizar): ").upper()
        if nombre.lower()=="salir":
            break  
        categoria = input("Ingrese la categoría del producto: ").upper()
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        nuevo_producto = Producto(nombre, categoria, precio, cantidad)
        inventario.agregarProducto(nuevo_producto)
        
    elif option==2: 
        nombre_producto = input("Ingrese el nombre del producto que desea actualizar: ").upper()
        actualizarProducto(nombre_producto, nuevo_precio, nueva_cantidad)
       
    elif option==3:
        nombre_producto= input("Ingrese el nombre del producto que desea eliminar: ").upper()
        inventario.eliminarProducto(nombre_producto)
    
    elif option==4:
        inventario.mostrarInventario()

    elif option==5:
        nombre_producto = input("Ingrese el nombre del producto que desea buscar: ").upper()
        inventario.buscarProducto(nombre_producto)
       
    elif option==6:
        print("Saliendo del programa...")
        break
    
    else:
     print("Opción inválida. Intente nuevamente.") 
         



    