"""
    Búsqueda Binaria

    Precondición: lista ordenada
    Devuelve -1 si x no está en la lista
    Devuelve p tal que lista[p] == x, si x esta en la lista
"""


def busqueda_binaria(lista, dato):
    izq = 0  # Guarda el índice del segmento
    der = len(lista) - 1  # Guarda el índice final del segmento

    # Un segmento es vacío cuando izq > der:
    while izq <= der:
        # Hallando el punto medio del segmento
        medio = int((izq + der)/2)

        if lista[medio] == dato:
            return medio

        # Si el valor del punto medio es mayor que el dato; sigue
        # buscando en el segmento de la izquierda: [izq, medio-1],
        # descartando la derecha
        elif lista[medio] > dato:
            der = medio - 1

        # Si no, sigue buscando en el segmento de la derecha:
        # [medio + 1, der], descartando la izquierda.
        else:
            izq = medio + 1

    return None  # Teniamos return -1


def buscar(dato, lista):
    if busqueda_binaria(lista, dato) == None:
        return "No se encontró el valor."
    else:
        return "El dato fue encontrado en la posición ", busqueda_binaria(lista, dato)


lista = [1, 2, 3, 5, 9]
print(buscar(3, lista))
