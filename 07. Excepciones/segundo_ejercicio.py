# Realiza una función llamada agregar_una_vez(lista, el) que reciba una lista y un elemento.
# La función debe añadir el elemento al final de la lista con la condición de no repetir ningún
# elemento. Además si este elemento ya se encuentra en la lista se debe invocar un error de tipo
# ValueError que debes capturar y mostrar este mensaje en su lugar:
lista = [1, 2, 3, 4, 5, 6, 7, 8]


def agregar_una_vez(lista, el):
    try:
        lista.append(el)
        return set(lista)
    except:
        raise(ValueError)


try:
    listita = agregar_una_vez(lista, 9)
except ValueError as ex:
    print(f'Ocurrió un error de tipo {ex}')
finally:
    print(listita)
