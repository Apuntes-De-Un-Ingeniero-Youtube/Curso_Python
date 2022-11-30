'''
    Escriba un programa que contenga dos listas, a continuación cree las
    siguientes listas donde no debe haber datos repetidos.

        *Lista de palabras que aparecen en las dos listas
        *Lista de palabras que aparecen en solo la primera lista
        *Lista de palabras que aparecen en solo la segunda lista
        *Lista de palabras que aparecen en ambas listas
'''
# Primer lista
lista1 = []
respuesta = input("¿Desea agregar elementos a la lista 1? (s/n) -> ")

while respuesta == "s" or respuesta == "S":
    lista1.append(input("Ingresa un nombre -> "))
    respuesta = input("¿Desea agregar elementos a la lista 1? (s/n) -> ")
print("Los elementos que ha ingresado en la lista 1 son: ", lista1)

# Primer lista
lista2 = []
respuesta = input("¿Desea agregar elementos a la lista 2? (s/n) -> ")

while respuesta == "s" or respuesta == "S":
    lista2.append(input("Ingresa un nombre -> "))
    respuesta = input("¿Desea agregar elementos a la lista 2? (s/n) -> ")
print("Los elementos que ha ingresado en la lista 2 son: ", lista2)

# Unión
union = list(set(lista1) | set(lista2))
print("Los elementos que aparecen en ambas listas son: ", union)

# Solo A
soloA = list(set(lista1) - set(lista2))
print("Los elementos que aparecen solo en la primer lista son: ", soloA)

# Solo B
soloB = list(set(lista2) - set(lista1))
print("Los elementos que aparecen solo en la primer lista son: ", soloB)

# Intersección
interseccion = list(set(lista1) & set(lista2))
print("Los elementos que se interceptan son: ", interseccion)
