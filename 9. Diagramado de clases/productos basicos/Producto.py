class Producto:
    contador_productos = 0

    def __init__(self, nombre, precio):
        Producto.contador_productos += 1
        self._id_producto = Producto.contador_productos
        self._nombre = nombre
        self._precio = precio

    @property
    def get_precio(self):
        return self._precio

    def __str__(self) -> str:
        return f"\n\nId producto: {self._id_producto}\nNombre: {self._nombre}\nPrecio: {self._precio}"


if __name__ == "__main__":
    producto1 = Producto("Procesador", 1000)
    print(producto1)
    producto2 = Producto("Tarjeta gráfica", 1700)
    print(producto2)
