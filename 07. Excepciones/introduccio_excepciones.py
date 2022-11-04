print('Antes del error')

def generador():
    yield 1
    print('Reanudando la ejecución')
    print('pescado')
    yield 2
    valor1 = 5
    valor2 = 7
    suma = valor1 + valor2
    yield suma

try:   
    gen = generador()
    print(type(gen))

    # Accediendo a sus valores
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
except:
    print('Ocurrió un error de divisíon.')
finally:
    print('Ejecutando algo')

print('Después del error')
print('otra línea')