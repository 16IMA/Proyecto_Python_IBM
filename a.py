
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
       