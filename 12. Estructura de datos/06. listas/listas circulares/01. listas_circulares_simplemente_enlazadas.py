class Nodo:

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaCircularSimplementeEnlazada:

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        return self.primero == None

    def agregar_inicio(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
            self.primero.siguiente = self.primero
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero = aux
            self.ultimo.siguiente = self.primero

    def agregar_final(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
            self.primero.siguiente = self.primero
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.siguiente = self.primero

    def recorrer(self):
        aux = self.primero
        while aux:
            print(aux.dato)
            aux = aux.siguiente
            if aux == self.primero:
                break

    def remover_inicio(self):
        if self.vacia():
            print("Lista vacía")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.primero = self.primero.siguiente
            self.ultimo.siguiente = self.primero

    def remover_final(self):
        if self.vacia():
            print("Lista vacía")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            aux = self.primero
            while aux.siguiente != self.ultimo:
                aux = aux.siguiente
            aux.siguiente = self.primero
            self.ultimo = aux


try:
    if __name__ == "__main__":
        opcion = 0
        lista = ListaCircularSimplementeEnlazada()
        while opcion != 7:
            print("--- Lista Simplemente Enlazada ---\n 1. Agregar último\n 2. Eliminar último\n 3. ¿Está vacía la lista?\n 4. Agregar Inicio\n 5. Eliminar Inicio\n 6. Mostrar\n 7. Salir")
            opcion = int(input("Ingrese su opción "))

            if opcion == 1:
                dato = input("Ingresa un número ")
                lista.agregar_final(dato)
            elif opcion == 2:
                lista.remover_final()
            elif opcion == 3:
                print("SI" if lista.vacia() else "NO")
            elif opcion == 4:
                dato = input("Ingresa un número ")
                lista.agregar_inicio(dato)
            elif opcion == 5:
                lista.remover_inicio()
            elif opcion == 6:
                lista.recorrer()
            elif opcion == 7:
                print("Adiós")
            else:
                print("Ingresaste una opción errónea, vuelve a intentarlo.")
except Exception as e:
    print(e)
