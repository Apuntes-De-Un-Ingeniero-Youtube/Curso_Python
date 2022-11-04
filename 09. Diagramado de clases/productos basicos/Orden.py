from Producto import Producto


class Orden:

    contador_ordenes = 0

    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._productos = list(productos)

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def calcular_orden(self):
        total = 0
        for producto in self._productos:
            total += producto.get_precio()
        return total

    def __str__(self) -> str:
        producto_str = ""
        for producto in self._productos:
            producto_str += producto.__str__() + "\n"
        return f"Orden: {self._id_orden}, \n Productos: {producto_str}"


if __name__ == "__main__":
    producto1 = Producto("Procesador i3", 500)
    producto2 = Producto("Procesador i7", 750)
    productos_lista = [producto1, producto2]
    orden1 = Orden(productos_lista)
    print(orden1)
    orden1.agregar_producto(Producto("Procesador i9", 1000))
    print(orden1)
    print(f"Toral orden: {orden1.calcular_orden()}")
