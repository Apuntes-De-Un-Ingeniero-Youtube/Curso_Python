"""
    Solicitar al usuario que ingrese números enteros positivos y, por cada uno,
    imprimir la suma de los dígitos que lo componen. 
    La condición de corte es que se ingrese el número -1. 
    Al finalizar, mostrar cuántos de los números ingresados por el usuario 
    fueron números pares.
"""
numero = int(input('Ingrese un número (-1 para finalizar el programa)  '))  # 730
pares = 0 # 1

while numero != -1:
    if numero % 2 == 0:
        pares += 1

    suma = 0
    if numero < 0:
        numero *= -1

    while numero != 0:
        digito = numero % 10  # 1
        suma += digito  # 16
        numero //= 10  # 0

    print(f'La suma de los dígitos es: {suma}')
    numero = int(input('Ingrese un número (-1 para finalizar el programa)  '))

print("Se ingresaron", pares, "números pares")
