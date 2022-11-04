"""
    Realizar un programa que realice de la suma de x numeros, dependiendo
    si son pares o impares, debe mostrar la suma de los números pares, los
    impares, la cantidad de números pares y la cantidad de números impares
"""

numero = int(input("Ingrese la acntidad de números que desea operar ")) # 4

pares = 0
impares = 0
contadorPares = 0
contadorImpares = 0

for iterador in range(numero): # 4
    num = int(input("Ingrese un número por favor  ")) # 7 8 21 13
    if num % 2 == 0:
        pares += num # 8
        contadorPares += 1 # 1
    else:
        impares += num # impares = impares + num  || 41
        contadorImpares += 1 # 3

print("\nHay ", contadorPares, " números pares y su suma es : ", pares,
      "\nHay ", contadorImpares, " números impares y su suma es : ", impares)
