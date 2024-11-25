class Invetario(Producto):

# Declaración de metodos

    def agregarProducto(self):
        nombre = input("Ingrese el nombre del producto: ")
        #verificar que no existe este producto
        categoria = input("Ingrese la categoría del producto: ")
        precio = int(input("Ingrese el precio del producto: "))
        #El precio debe ser siempre mayor que 0.
        cantidad = int(input("Ingrese la cantidad del producto: "))
        #La cantidad debe ser mayor o igual que 0.
        producto1 = Producto(nombre, categoria, precio,)
print("Producto agregado correctamente.") #comprobar que ha introducido todo


    def actualizarProducto(self):
        input("Indique el nombre del producto que desea actualizar: ")
        #bucle for para buscar nombre de producto?
        print(lista_nombre_seleccionado)
        print("1. Modificar precio del producto")
        print("2. Modificar cantidad del producto")
        option_change= int(input("Indique el dato del producto que desea actualizar: "))
            if option_change==1:
                input("Ingrese el nuevo precio del producto: ")
            elif option_change==2:
                input("Ingrese la nueva cantidad del producto: ")
            else:
                print("Opción no válida.")
        print(nueva_lista)
        print("Producto actualizado correctamente.")

    def eliminarProducto(self):
        input("Ingrese el nombre del producto que desea eliminar: ")
       #bucle for para buscar nombre de producto?
       print(lista_nombre_seleccionado)
       print("¿Está seguro de eliminar este producto? (S/N): ")
       confirmacion=input()
            if confirmacion.upper()=="S":
                    del(lista_producto)
                    print("Producto eliminado correctamente.")
            else:
                    print("Eliminación cancelada")
    
    def mostrarInventario(self):
        input("Ingrese el nombre del producto que desea buscar: ")
        #bucle for para buscar nombre de producto?
        print(lista_nombre_seleccionado)

    def buscarProducto(self):
        input("Ingrese el nombre del producto que desea buscar: ")
        #bucle for para buscar nombre de producto?
        print(lista_nombre_seleccionado)

    def salir(self):
        print("¿Está seguro de que quiere salir de la aplicación? (S/N): ")
        confirmacion=input()
            if confirmacion.upper()=="S":
                    exit()
            else:
            print("¡Continuamos trabajando!")          