pares = []
impares = []

for numero in range(10):
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f'Pares: {pares} \n Impares: {impares}')

# El mismo ejercicio con List Comprehension
pares = []
impares = []
[pares.append(numero) if numero % 2 == 0 else impares.append(numero) for numero in range(10)]
print(f'Pares: {pares} \n Impares: {impares}')


