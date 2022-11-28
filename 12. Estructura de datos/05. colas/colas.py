class Cola:

    def __init__(self):
        self.cola = []
        self.size = 0

    # Si esta vacía la cola
    def empty(self):
        return len(self.cola) == 0

    # Agregar datos a la cola
    def push(self, dato):
        self.cola += [dato]
        self.size += 1

    # Eliminar un elemento de la cola
    def pop(self):
        if self.empty():
            print("La cola está vacia")
        else:
            self.cola = [self.cola[i] for i in range(1, self.size)]
            self.size -= 1

    # Mostrar la cola
    def show(self):
        n = self.size - 1
        while n > -1:
            print(f"[{n}] => {self.cola[n]}")
            n -= 1

    # Mostrar primer dato de la cola
    def front(self):
        print("Cola vacía") if self.empty() else print(
            "Primer dato ", self.cola[0])


try:
    if __name__ == "__main__":
        opcion = 0
        cola = Cola()
        while opcion != 6:
            print("--- Colas ---\n 1. Agregar dato\n 2. Eliminar dato\n 3. ¿Está vacía la cola?\n 4. Mostrar cola\n 5. Mostrar primero\n 6. Salir")
            opcion = int(input("Ingrese su opción "))

            if opcion == 1:
                dato = input("Ingresa un número ")
                cola.push(dato)
            elif opcion == 2:
                cola.pop()
            elif opcion == 3:
                print("SI" if cola.empty() else "NO")
            elif opcion == 4:
                cola.show()
            elif opcion == 5:
                print(cola.front())
            elif opcion == 6:
                print("\n--- Sesión culminada ---")
            else:
                print("Ingresaste una opción errónea, vuelve a intentarlo.")
except Exception as e:
    print(e)
