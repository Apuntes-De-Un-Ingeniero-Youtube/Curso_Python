arreglo = [11, 65, 23, 3, 4, 5, 6, 77, 123, 54, 23, 90, 0]


def busqueda_lineal(dato):
    for x in range(len(arreglo)):
        if arreglo[x] == dato:
            return x
    return None


def buscar(dato):
    if busqueda_lineal(dato) == None:
        return "El dato %d no se encontró en el arreglo" % (dato)
    else:
        return f"El dato {dato} se encontró en el índice {busqueda_lineal(dato)}"


print(buscar(77))
