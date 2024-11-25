def actualizarPrecio(self, precio, nuevo_precio):
        Producto.precio= precio         
     
    def eliminarProducto(self, nombre):
        indice_producto= lista_producto.index(nombre)
        lista_producto.remove(indice_producto)  
        
    
    def mostrarInventario(self, nombre):
        indice_producto= lista_producto.index(nombre)
        print(lista_producto[indice_producto:])
        

    def buscarProducto(self, listas_productos, producto_buscado):
        for j in listas_productos:
            if j == producto_buscado:
                return j

    def salir(self):
        print("¿Está seguro de que quiere salir de la aplicación? (S/N): ")
        confirmacion=input()
            if confirmacion.upper()=="S":
                    exit()
            else:
            print("¡Continuamos trabajando!")         