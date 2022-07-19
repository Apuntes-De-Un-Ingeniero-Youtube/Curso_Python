# Un generador no es mas que una función especial de Python que no tiene return sino que
# utiliza la palabra reservada yield (reservar o generar)

# def funcion():
#     arr = [1, 2, 3]
#     return arr;

# arr2 = funcion()
# print(arr2[0])

def generador():
    yield 1
    print('Reanudando la ejecución')
    print('pescado')
    yield 2
    valor1 = 5
    valor2 = 7
    suma = valor1 + valor2
    yield suma


gen = generador()
print(type(gen))

# Accediendo a sus valores
print(next(gen))
print(next(gen))
print(next(gen))

for valor in generador():
    print(f'Valor devuelto {valor}')
