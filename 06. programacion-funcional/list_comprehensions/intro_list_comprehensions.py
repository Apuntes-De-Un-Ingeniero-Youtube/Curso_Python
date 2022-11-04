numeros = range(10)
lista_pares = []

# Crear un array que almacene los valores pares multiplicados entre por si mismos de un rango
# determinado
for numero in numeros:
    if numero % 2 == 0:
        lista_pares.append(numero * numero)

print(f'Lista pares duplicados -> {lista_pares}')

lista_pares = []
lista_pares = [numero * numero for numero in numeros if numero % 2 == 0]
print(f'Lista pares con list comprehensions -> {lista_pares}')
