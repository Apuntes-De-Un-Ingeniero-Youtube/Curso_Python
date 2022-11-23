class Pila:

    def __init__(self, size):
        self.lista = []
        self.tope = 0
        self.size = size

    # Si hay elementos en la pila o sea en la lista
    def empty(self):
        if self.tope == 0:
            return True
        else:
            return False

    # Agregar datos a la pila
    def push(self, dato):
        if self.tope < self.size:
            self.lista += [dato]
            self.tope += 1
        else:
            self.size += 5
            self.lista += [dato]
            self.tope += 1

    # Eliminar datos
    def pop(self):
        if self.empty():
            print("La pila está vacía")
        else:
            self.tope -= 1
            self.lista = [self.lista[x] for x in range(self.tope)]

    # Mostrar pila
    def show(self):
        i = self.tope - 1
        while i > -1:
            print(f"[{i}] => {self.lista[i]}")
            i -= 1

    # Mostrando la cima de la pila
    def top(self):
        return self.lista[-1]


if __name__ == "__main__":
    opcion = 0
    pila = Pila(5)
    while opcion != 6:
        print("--- Pilas ---\n 1. Agregar dato\n 2. Eliminar\n 3. ¿Está vacía a pila?\n 4. Mostrar pila\n 5. Mostrar cima\n 6. Salir")
        opcion = int(input("Ingrese su opción "))

        if opcion == 1:
            dato = int(input("Ingresa un número "))
            pila.push(dato)
        elif opcion == 2:
            pila.pop()
        elif opcion == 3:
            print("SI" if pila.empty() else "NO")
        elif opcion == 4:
            pila.show()
        elif opcion == 5:
            print(pila.top())
        elif opcion == 6:
            print("\n--- Sesión culminada ---")
        else:
            print("Ingresaste una opción errónea, vuelve a intentarlo.")
