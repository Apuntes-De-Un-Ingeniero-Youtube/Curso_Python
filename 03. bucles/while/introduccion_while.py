# contador = 0
# while contador < 8:
#     print("El numero esta entre 3 y 8")
#     contador += 1

"""
    Leer números enteros de teclado, hasta que el usuario ingrese el 0. 
    Finalmente, mostrar la sumatoria de todos los números ingresados.
"""
numero = int(input('Ingrese un número ')) #7
sumatoria = 0 #7

while numero != 0:
    if numero == 3:
        break
    sumatoria += numero
    numero = int(input('Ingrese un número '))

print(sumatoria)

