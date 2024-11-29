#Creamos las clases Producto e Inventario

class Producto():

#Constructor de clase.

    def __init__(self, nombre, categoria, precio, cantidad):

#Validaciones mediante assert (saltan al crear objeto).

        assert isinstance(nombre, str) and nombre.strip(), "El nombre debe ser un texto y no puede estar vacío." #No podrán incluir un nombre con input vacío
        assert isinstance(categoria, str) and categoria.strip(), "La categoría debe ser un texto y no puede estar vacía." #No podrán incluir una categoría con input vacío
        assert precio > 0, "El precio debe ser mayor a 0." #No podrán incluir un precio menor o igual a 0.
        assert cantidad >= 0, "La cantidad no puede ser menor a 0." #No podrán incluir un precio menor a 0.

#Establecemos los atributos de la clase (encapsulados o privados).

        self.__nombre = nombre.upper() #Para evitar errores y duplicar nombres convertimos el texto a mayúsculas.
        self.__categoria = categoria.upper() #Para evitar errores y duplicar categorías convertimos el texto a mayúsculas.
        self.__precio = precio
        self.__cantidad = cantidad

#Incorporamos getters y setters para consultar o actualiar los atributos privados.

    @property
    def nombre(self):
        return self.__nombre #Solo hay getter de consulta ya que es un atributo que no se puede actualizar.

    @property
    def categoria(self):
        return self.__categoria #Solo hay getter de consulta ya que es un atributo que no se puede actualizar.

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, precio):
        if not isinstance(precio, (float)) or precio <= 0:
            raise ValueError("El precio debe ser un número mayor a 0.") #Incluimos una validación en el setter para evitar que introduzcan datos que sean menores o iguales a 0.
        self.__precio = precio

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, cantidad):
        if not isinstance(cantidad, int) or cantidad < 0:
            raise ValueError("La cantidad debe ser un número entero mayor o igual a 0.") #Incluimos una validación en el setter para evitar que introduzcan datos que sean menores a 0.
        self.__cantidad = cantidad

class Inventario():

#Constructor de clase.

#Iniciamos una lista.

    def __init__(self):
        self.productos = []

#Declaración de metodos.

#Método agregar productos.

    def agregarProducto(self, producto):
        for prod in self.productos:
            if prod.nombre == producto.nombre: #Busca el producto por el nombre en la lista del inventario para evitar repetir el mismo producto, si ya existe lanza un error.
                print(f"\nError: El producto '{producto.nombre}' ya existe en el inventario.")
                return


        self.productos.append(producto)
        print(f"\nProducto '{producto.nombre}' agregado correctamente.")

#Método eliminar productos.

    def eliminarProducto(self, nombre_producto):
        for producto in self.productos:
              if producto.nombre == nombre_producto: #Busca el producto por el nombre en la lista del inventario para poder eliminarlo de la lista del inventario.
                    self.productos.remove(producto)
                    print("\nProducto eliminado")
                    return
        print("\nProducto inexistente") #Si no existe el nombre del producto vuelve al menú principal.

#Método actualizar productos.

    def actualizarProducto(self, nombre_producto, nuevo_precio, nueva_cantidad):
        for producto in self.productos:
            if producto.nombre == nombre_producto: #Busca el producto por el nombre en la lista del inventario y confirma que existe para actualizar los atributos del producto.
                print(f"\nProducto encontrado: {producto.nombre}\n")
                print("\n-Actualizar producto-\n") #Abrimos con un título porque se despliega un nuevo menú de selección. Deben elegir entre modificar el precio o la cantidad. El resto de atributos no se modifican en este caso.
                print("1. Actualizar precio")#Debe elegir una de las dos opciones.
                print("2. Actualizar cantidad\n")
                while True:
                    try:
                        opcion = int(input("\nSeleccione qué desea actualizar: "))
                        if opcion == 1:
                          nuevo_precio = float(input(f"\nIngrese el nuevo precio (actual: {producto.precio}): "))
                          try:
                            producto.precio = nuevo_precio
                          except ValueError as e:
                                print(f"\nError: {e}")
                                continue

                          print(f"\nPrecio actualizado correctamente a {producto.precio}.")
                          return


                        elif opcion == 2:
                          nueva_cantidad = int(input(f"\nIngrese la nueva cantidad (actual: {producto.cantidad}): "))
                          try:
                            producto.cantidad = nueva_cantidad
                          except ValueError as e:
                            print(f"\nError: {e}")
                            continue

                          print(f"\nCantidad actualizada correctamente a {producto.cantidad}.")
                          return

                        else:
                            print("\nOpción inválida. Inténtelo nuevamente.")
                            continue

                    except ValueError:
                        print("\nError: Debe ingresar un valor numérico para la opción. Inténtelo de nuevo.") #En la selección de la opción verificamos que elijan un int.
                    continue

        print(f"\nProducto '{nombre_producto}' no encontrado.")


#Método buscar productos.

    def buscarProducto(self, nombre_producto):
        for producto in self.productos:
            if producto.nombre == nombre_producto: #Busca el producto por el nombre en la lista del inventario.
                print("\nProducto encontrado:")
                print(
                    f"\nNombre: {producto.nombre}, Categoría: {producto.categoria}, "  #Muestra todos los atributos del producto.
                    f"Precio: {producto.precio}, Cantidad: {producto.cantidad}"
                )
                return
        print(f"No se encontró un producto con el nombre '{nombre_producto}'.")  #Indica que no se encontró el nombre del producto en el inventario.


#Método mostrar Inventario.

    def mostrarInventario(self):
        if not self.productos:
            print("\nEl inventario está vacío.")
        else:
            print("\nInventario actual:\n")
            for producto in self.productos:
                  print(f"Nombre del producto: {producto.nombre}, categoría: {producto.categoria}, precio: {producto.precio}, cantidad: {producto.cantidad}")


#Programa principal.

inventario = Inventario()

#Iniciamos bucle para llamar a la función menú y ejecutar programa.

while True: #Bucle que permite visualizar el menú una y otra vez sin salir del programa.
    print("\n— Menú de Inventario —\n")
    print("1.Agregar producto")
    print("2.Actualizar producto")
    print("3.Eliminar producto")
    print("4.Mostrar inventario")
    print("5.Buscar producto")
    print("6.Salir")

    try:
        option= int(input("\nSeleccionar una opción: ")) #En la selección de la opción verificamos que elijan un int.
    except ValueError:
        print("\nError: Debe ingresar un valor numérico para la opción.")
        continue


    if option==1:
        print("\n- Agregar productos -\n")

        nombre = input("Ingrese el nombre del producto: ").upper() #Es importante mencionar que toda la información en texto debe pasar a mayúsculas.
        categoria = input("Ingrese la categoría del producto: ").upper()

        try:
            precio = float(input("Ingrese el precio del producto: "))
        except ValueError:
            print("\nError: Debe ingresar un valor numérico para el precio. Recuerde utilizar punto . y no coma , para separar los decimales.") #Hemos establecido que solo se pueden introducir valores float.
            continue
        try:
          cantidad = int(input("Ingrese la cantidad del producto: "))
        except ValueError:
            print("\nError: Debe ingresar un valor numérico para la cantidad.") #Hemos establecido que solo se pueden introducir valores int.
            continue


        try:
          nuevo_producto = Producto(nombre, categoria, precio, cantidad) #Creamos un nuevo objeto.
          inventario.agregarProducto(nuevo_producto) #Introducimos el objeto en una lista de inventario.

        except AssertionError as e: #Hemos establecido un assert en el setter para evitar que los valores sean menores a 0.
          print(f"\nError: {e}")




    elif option==2:

        nombre_producto = input("\n-Ingrese el nombre del producto que desea actualizar: ").upper()
        inventario.actualizarProducto(nombre_producto, nuevo_precio=None, nueva_cantidad=None) #Llamamos al método del inventario actualizarProducto

    elif option==3:
        nombre_producto= input("\n-Ingrese el nombre del producto que desea eliminar: ").upper()
        inventario.eliminarProducto(nombre_producto) #Llamamos al método del inventario eliminarProducto

    elif option==4:
        inventario.mostrarInventario() #Llamamos al método del inventario mostrarProducto

    elif option==5:
        nombre_producto = input("\n-Ingrese el nombre del producto que desea buscar: ").upper()
        inventario.buscarProducto(nombre_producto) #Llamamos al método del inventario buscarProducto

    elif option==6:
        print("\n-Saliendo del programa. ¡Hasta la próxima!")
        break #Permite salir del programa

    else:
     print("\n-Opción inválida. Intente nuevamente.") #Si no eligen un int que se encuentre entre las opciones del 1 al 6, vuelve al menú principal.