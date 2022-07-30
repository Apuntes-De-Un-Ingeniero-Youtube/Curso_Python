# Crear un script en Python que permita agregar a una lista o un
# vector los números que sean divisibles entre 2 y entre 6 en un
# rango especificado por el usuario (a, b), esto utilizando list comprehensions.

# Realizando el ejercicio sin list comprehensions.
A = int(input('Ingrese el límite inferior del rango '))  # 4
B = int(input('Ingrese el límite superior del rango '))  # 30
vector = []

for i in range(A, B, 1):
    if i % 2 == 0 and i % 6 == 0:
        vector.append(i)

print(
    f'Vector números divisibles entre 2 y 6 en un rango {A}, {B} -> {vector}')

# Solución del ejercicio empleando List Comprehensions
vector = [numero for numero in range(
    A, B, 1) if numero % 2 == 0 if numero % 6 == 0]
print(
    f'LVector números divisibles entre 2 y 6 en un rango {A}, {B} -> {vector}')
