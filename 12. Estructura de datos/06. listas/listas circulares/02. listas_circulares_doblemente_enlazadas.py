class Nodo:

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None


class ListaCircularDoblementeEnlazada:

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def __unir_nodos(self):
        if self.primero != None:
            self.primero.anterior = self.ultimo
            self.ultimo.siguiente = self.primero

    def vacia(self):
        return self.primero == None

    def agregar_inicio(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux
        self.__unir_nodos()

    def agregar_final(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.anterior = aux
        self.__unir_nodos()

    def recorrer_inicio_fin(self):
        aux = self.primero
        while aux:
            print(aux.dato)
            aux = aux.siguiente
            if aux == self.primero:
                break

    def recorrer_fin_inicio(self):
        aux = self.ultimo
        while aux:
            print(aux.dato)
            aux = aux.anterior
            if aux == self.ultimo:
                break

    def eliminar_inicio(self):
        if self.vacia():
            print("Lista vacía")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.primero = self.primero.siguiente
        self.__unir_nodos()

    def eliminar_final(self):
        if self.vacia():
            print("Lista vacía")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.ultimo = self.ultimo.anterior
        self.__unir_nodos()

    def buscar(self, dato):
        aux = self.primero
        while aux:
            if aux.dato == dato:
                return True
            else:
                aux = aux.siguiente
                if aux == self.primero:
                    return False


try:
    if __name__ == "__main__":
        opcion = 0
        lista = ListaCircularDoblementeEnlazada()
        while opcion != 9:
            print("--- Lista Circular Doblemente Enlazada ---"
                  + "\n 1. Agregar último"
                  + "\n 2. Eliminar último"
                  + "\n 3. ¿Está vacía la lista?"
                  + "\n 4. Agregar Inicio"
                  + "\n 5. Eliminar Inicio"
                  + "\n 6. Mostrar de inicio a fin\n 7. Mostrar de fin a inicio\n 8. Buscar un dato\n 9. Salir")
            opcion = int(input("Ingrese su opción "))

            if opcion == 1:
                dato = input("Ingresa un número ")
                lista.agregar_final(dato)
            elif opcion == 2:
                lista.eliminar_final()
            elif opcion == 3:
                print("SI" if lista.vacia() else "NO")
            elif opcion == 4:
                dato = input("Ingresa un número ")
                lista.agregar_inicio(dato)
            elif opcion == 5:
                lista.eliminar_inicio()
            elif opcion == 6:
                lista.recorrer_inicio_fin()
            elif opcion == 7:
                lista.recorrer_fin_inicio()
            elif opcion == 8:
                dato = input("Ingresa el dato a buscar")
                print("El dato fue encontrado" if lista.buscar(
                    dato) else "El dato no ha sido encontrado")
            elif opcion == 9:
                print("Adiós")
            else:
                print("Ingresaste una opción errónea, vuelve a intentarlo.")
except Exception as e:
    print(e)
