"""
    Escribir un programa que permita almacenar n números naturales en una lista 
    y la ordene de manera inversa.
"""
lista = []

ingresa = input("¿Desea ingresa un número? (s/n) -> ")
while ingresa == "s" or ingresa == "S":
    lista.append(int(input("Ingresa un número -> ")))
    ingresa = input("¿Desea ingresa un número? (s/n) -> ")

lista.sort(reverse=True)
print(lista)
