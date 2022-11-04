# Las expresiones generadoras no son mas que una función generadora de caracter anónimo
rango = int(input('Ingrese un número por favor '))

# (yield funcion condicional)
generador = (numero * numero for numero in range(rango))

print(type(generador))
# print(next(generador))
# print(next(generador))
# print(next(generador))
# print(next(generador))
# print(next(generador))
# print(next(generador))
# print(next(generador))

for valor in generador:
    print(f'Valor generado -> {valor}')
