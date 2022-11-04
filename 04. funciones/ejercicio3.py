"""
Escribir un programa que pida números al usuario, 
motrar el factorial de cada uno y, al finalizar, la cantidad total de números leídos en total. 
Utilizar una o más funciones, según sea necesario.
"""


def factorial(numero): # 5
    f = 1 # 120
    if numero != 0:
        for i in range(1, numero + 1): # 1, 6
            f = f * i # 120
    return f


cantidad = 0
num = int(input('Ingrese un múmero (-1 para salir): '))

while num != -1:
    print(f'Factorial de {num} = {factorial(num)}')
    cantidad = cantidad + 1
    num = int(input('Ingrese un múmero (-1 para salir): '))

print(f'Se leyeron {cantidad} numeros')
