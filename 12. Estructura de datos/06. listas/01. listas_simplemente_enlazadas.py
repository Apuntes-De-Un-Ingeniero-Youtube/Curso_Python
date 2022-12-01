class Nodo:

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaSimplememteEnlazada:

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        return self.primero == None

    def agregar_ultimo(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)

    def recorrido(self):
        aux = self.primero
        while aux != None:
            print(aux.dato)
            aux = aux.siguiente

    def eliminar_ultimo(self):
        aux = self.primero
        while aux.siguiente != self.ultimo:
            aux = aux.siguiente
        aux.siguiente = None
        self.ultimo = aux

    def agregar_inicio(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero = aux

    def eliminar_inicio(self):
        self.primero = self.primero.siguiente


try:
    if __name__ == "__main__":
        opcion = 0
        lista = ListaSimplememteEnlazada()
        while opcion != 7:
            print("--- Lista Simplemente Enlazada ---\n 1. Agregar último\n 2. Eliminar último\n 3. ¿Está vacía la lista?\n 4. Agregar Inicio\n 5. Eliminar Inicio\n 6. Mostrar\n 7. Salir")
            opcion = int(input("Ingrese su opción "))

            if opcion == 1:
                dato = input("Ingresa un número ")
                lista.agregar_ultimo(dato)
            elif opcion == 2:
                lista.eliminar_ultimo()
            elif opcion == 3:
                print("SI" if lista.vacia() else "NO")
            elif opcion == 4:
                dato = input("Ingresa un número ")
                lista.agregar_inicio(dato)
            elif opcion == 5:
                lista.eliminar_inicio()
            elif opcion == 6:
                lista.recorrido()
            elif opcion == 7:
                print("Adiós")
            else:
                print("Ingresaste una opción errónea, vuelve a intentarlo.")
except Exception as e:
    print(e)
