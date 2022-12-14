class Nodo:

    def __init__(self, valor=None, padre=None, es_raiz=False, es_izquierda=False, es_derecha=False):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.padre = padre
        self.es_raiz = es_raiz
        self.es_izquierda = es_izquierda
        self.es_derecha = es_derecha


class ArbolBinarioBusqueda:

    def __init__(self):
        self.raiz = None

    # Esa vacío el árbol
    def vacio(self):
        return self.raiz == None

    def __obtener_lugar(self, valor):
        aux = self.raiz
        while aux != None:
            temp = aux
            if valor <= aux.valor:
                aux = aux.izquierda
            else:
                aux = aux.derecha
        return temp

    # Agregar datos al árbol
    def agregar(self, valor):
        if self.vacio():
            self.raiz = Nodo(valor=valor, es_raiz=True)
        else:
            nodo = self.__obtener_lugar(valor)
            if valor <= nodo.valor:
                nodo.izquierda = Nodo(
                    valor=valor, padre=nodo, es_izquierda=True)
            else:
                nodo.derecha = Nodo(valor=valor, padre=nodo, es_derecha=True)

    def recorrido_in_orden(self, node):
        if node:
            self.recorrido_in_orden(node.izquierda)
            print(node.valor)
            self.recorrido_in_orden(node.derecha)

    def recorrido_in_pre_orden(self, node):
        if node:
            print(node.valor)
            self.recorrido_in_pre_orden(node.izquierda)
            self.recorrido_in_pre_orden(node.derecha)

    def recorrido_in_pos_orden(self, node):
        if node:
            self.recorrido_in_pos_orden(node.izquierda)
            self.recorrido_in_pos_orden(node.derecha)
            print(node.valor)

    def buscar(self, nodo, valor):
        if nodo == None:
            return None
        else:
            if nodo.valor == valor:
                return nodo
            elif valor <= nodo.valor:
                return self.buscar(nodo.izquierda, valor)
            else:
                return self.buscar(nodo.derecha, valor)


if __name__ == "__main__":

    def menu():
        opc = 0
        arbol_binario = ArbolBinarioBusqueda()
        try:
            while opc != 7:
                print("\nDiccionario Artículos\n"
                      + "\n\t1. Agregar Datos"
                      + "\n\t2. ¿Esta vacío el árbol?"
                      + "\n\t3. Recorrer en orden"
                      + "\n\t4. Recorrer en post-orden"
                      + "\n\t5. Recorrer en pre-orden"
                      + "\n\t6. Buscar"
                      + "\n\t7. Salir")

                opc = int(input("Ingrese su opción "))

                if opc == 1:
                    dato = int(input("Ingrese el dato a anexar al arbol "))
                    arbol_binario.agregar(dato)
                elif opc == 2:
                    print("SI" if arbol_binario.vacio() else "NO")
                elif opc == 3:
                    arbol_binario.recorrido_in_orden(arbol_binario.raiz)
                elif opc == 4:
                    arbol_binario.recorrido_in_pos_orden(arbol_binario.raiz)
                elif opc == 5:
                    arbol_binario.recorrido_in_pre_orden(arbol_binario.raiz)
                elif opc == 6:
                    dato = int(input("Ingrese el dato a buscar en el arbol "))
                    print(arbol_binario.buscar(arbol_binario.raiz, dato))
                elif opc == 7:
                    print("Adios")
                else:
                    print("Ingresaste una opción errónea")
        except Exception as e:
            print("\n Solo se permiten caracteres numéricos")
            print(e)

    menu()
