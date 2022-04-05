"""
    Leer un número entero positivo desde teclado e imprimir la suma de 
    los dígitos que lo componen.
"""
numero = int(input('Ingrese un número entero positivo '))  # 1834
suma = 0

if numero < 0:
    numero *= -1

while numero != 0:
    digito = numero % 10  # 1
    suma += digito  # 16
    numero //= 10  # 0


print(f'La suma de los digitos del número es igual {suma}')
