class Producto():

#Constructor de clase

    def __init__(self, nombre, categoria, precio, cantidad):
        
        self.nombre = nombre  
        self.categoria = categoria  
        self.precio = precio  
        self.cantidad = cantidad  

#Incorporamos Getters y setters

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser un texto.")
        self.__nombre = nombre.upper()

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, categoria):
        if not isinstance(categoria, str):
            raise ValueError("La categoría debe ser un texto.")
        self.__categoria = categoria.upper()

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, precio):
        if not isinstance(precio, (int, float)) or precio <= 0:
            raise ValueError("El precio debe ser un número mayor a 0.")
        self.__precio = precio

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, cantidad):
        if not isinstance(cantidad, int) or cantidad < 0:
            raise ValueError("La cantidad debe ser un número entero mayor o igual a 0.")
        self.__cantidad = cantidad

class Inventario():

#Constructor de clase

#Iniciamos una lista

    def __init__(self):
        self.productos = []

#1Declaración de metodos

#Método agregar productos
    
    def agregarProducto(self, producto):
        for prod in self.productos:
            if prod.nombre == producto.nombre: #Busca el producto por el nombre en la lista del inventario para evitar repetir el mismo producto
                print(f"Error: El producto '{producto.nombre}' ya existe en el inventario.")
                return


        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado correctamente.")

#Método eliminar productos

    def eliminarProducto(self, nombre_producto):
        for producto in self.productos:
              if producto.nombre == nombre_producto: #Busca el producto por el nombre en la lista del inventario para poder eliminarlo de la lista del inventario
                    self.productos.remove(producto)
                    print("Producto eliminado")
                    return
        print("Producto inexistente")

#Método actualizar productos

    def actualizarProducto(self, nombre_producto, nuevo_precio, nueva_cantidad):
        for producto in self.productos:
            if producto.nombre == nombre_producto: #Busca el producto por el nombre en la lista del inventario y confirma que existe para actualizar los atributos del producto
                print(f"Producto encontrado: {producto.nombre}\n")
                print("1. Actualizar precio")
                print("2. Actualizar cantidad\n")
                while True:  #Bucle para asegurarse de manejar entradas inválidas
                    try:
                        opcion = int(input("Seleccione qué desea actualizar: "))
                        if opcion == 1:
                            while True:   #Bucle para asegurarse de manejar entradas inválidas
                                try:
                                    nuevo_precio = float(input(f"Ingrese el nuevo precio (actual: {producto.precio}): "))
                                    producto.precio = nuevo_precio
                                    print(f"Precio actualizado correctamente a {producto.precio}.")
                                    return
                                except ValueError:
                                    print("Error: Debe ingresar un valor numérico para el precio. Inténtelo de nuevo.")
                                    continue
                        elif opcion == 2:
                            while True: #Bucle para asegurarse de manejar entradas inválidas
                                try:
                                    nueva_cantidad = int(input(f"Ingrese la nueva cantidad (actual: {producto.cantidad}): "))
                                    producto.cantidad = nueva_cantidad
                                    print(f"Cantidad actualizada correctamente a {producto.cantidad}.")
                                    return
                                except ValueError:
                                    print("Error: Debe ingresar un valor numérico para la cantidad. Inténtelo de nuevo.")
                                    continue
                        else:
                            print("Opción inválida. Inténtelo nuevamente.")
                    except ValueError:
                        print("Error: Debe ingresar un valor numérico para la opción. Inténtelo de nuevo.")
                    return
        print(f"Producto '{nombre_producto}' no encontrado.")


#Método buscar productos

    def buscarProducto(self, nombre_producto):
        for producto in self.productos:
            if producto.nombre == nombre_producto: #Busca el producto por el nombre en la lista del inventario
                print(
                    f"Nombre: {producto.nombre}, Categoría: {producto.categoria}, "  #Muestra todos los atributos del producto
                    f"Precio: {producto.precio}, Cantidad: {producto.cantidad}"
                )
                return  
        print(f"No se encontró un producto con el nombre '{nombre_producto}'.")  #Indica que no se encontró el nombre del producto en el inventario


#Método mostrar Inventario

    def mostrarInventario(self):
         for producto in self.productos:
              print(f"Nombre del producto: {producto.nombre}, categoría: {producto.categoria}, precio: {producto.precio}, cantidad: {producto.cantidad}")


#Programa principal

inventario = Inventario()

#Iniciamos bucle para llamar a la función menú y ejecutar programa

while True: #Bucle que permite visualizar el menú una y otra vez sin salir del programa
    print("\n— Menú de Inventario —\n")
    print("1.Agregar producto")
    print("2.Actualizar producto")
    print("3.Eliminar producto")
    print("4.Mostrar inventario")
    print("5.Buscar producto")
    print("6.Salir")

    try:
        option= int(input("\nSeleccionar una opción: "))
    except ValueError:
        print("Error: Debe ingresar un valor numérico para la opción.")
        continue


    if option==1:
        print("\n- Agregar productos -\n")

        nombre = input("Ingrese el nombre del producto: ").upper()
        categoria = input("Ingrese la categoría del producto: ").upper()

        try:
            precio = float(input("Ingrese el precio del producto: "))
        except ValueError:
            print("Error: Debe ingresar un valor numérico para el precio. Recuerde utilizar punto . y no coma , para separar los decimales.")
            continue

        try:
          cantidad = int(input("Ingrese la cantidad del producto: "))
        except ValueError:
            print("Error: Debe ingresar un valor numérico para la cantidad.")
            continue

        nuevo_producto = Producto(nombre, categoria, precio, cantidad)
        inventario.agregarProducto(nuevo_producto)


    elif option==2:

        nombre_producto = input("Ingrese el nombre del producto que desea actualizar: ").upper()
        inventario.actualizarProducto(nombre_producto, nuevo_precio=None, nueva_cantidad=None)

    elif option==3:
        nombre_producto= input("Ingrese el nombre del producto que desea eliminar: ").upper()
        inventario.eliminarProducto(nombre_producto)

    elif option==4:
        inventario.mostrarInventario()

    elif option==5:
        nombre_producto = input("Ingrese el nombre del producto que desea buscar: ").upper()
        inventario.buscarProducto(nombre_producto)

    elif option==6:
        print("Saliendo del programa. ¡Hasta la próxima!")
        break

    else:
     print("Opción inválida. Intente nuevamente.")
