#CREACIÓN DE CLASES

class Producto():
# Declaración de atributos
    def __init__(self, nombre, categoria, precio, cantidad): 
    self.nombre= nombre 
    self.categoria= categoria
    self.precio= precio
    self.cantidad= cantidad

class Invetario():
# Declaración de atributos

    nombre= Producto.nombre 
    categoria= Producto.categoria
    precio= Producto.precio
    cantidad= Producto.cantidad



# Declaración de metodos

    def agregarProducto(self):
        nombre = input("Ingrese el nombre del producto: ")
        #verificar que no existe este producto
        categoria = input("Ingrese la categoría del producto: ")
        precio = int(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
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












    def __init__(self):
        self.lista_productos=[]

    def agregar_producto(self, producto):
        self.lista_productos.append(producto) #INVESTIGAR COMO FUNCIONA LA AUTOMATIZACIÓN DE RELLENAR OBJETOS Y APLICAR EL INVENTARIO 

i=0
while i==0:
  print("— Menú de Inventario —")
  print("1.Agregar producto")
  print("2.Actualizar producto")
  print("3.Eliminar producto")
  print("4.Mostrar inventario")
  print("5.Buscar producto")
  print("6.Salir")
  option= int(("Seleccionar una opción: "))

  

   if option==1:
        nombre = input("Ingrese el nombre del producto: ")
        #verificar que no existe este producto
        categoria = input("Ingrese la categoría del producto: ")
        precio = int(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        producto1 = Producto(nombre, categoria, precio,)
print("Producto agregado correctamente.") #comprobar que ha introducido todo

    
    elif option==2:
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


    elif option==3:
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

    
    elif option==4:
      print("--Inventario--")
      print(todas_las_listas)
    
    elif option==5:
        input("Ingrese el nombre del producto que desea buscar: ")
        #bucle for para buscar nombre de producto?
        print(lista_nombre_seleccionado)
        
    
    elif option==6:
       print("¿Está seguro de que quiere salir de la aplicación? (S/N): ")
       confirmacion=input()
            if confirmacion.upper()=="S":
                    exit()
            else:
            print("¡Continuamos trabajando!")        
       