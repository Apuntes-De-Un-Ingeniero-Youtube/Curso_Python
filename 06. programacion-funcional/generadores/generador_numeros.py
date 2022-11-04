# Craer una función generadora que se encargue de generar automáticamente una cantidad de números
# itroducidos por el usuario en un rango determinado.

rango = int(input('Ingrese el rango de números a generar. '))  # 5

# Creando el generador de n números
def generador_numeros(rang):
    for numero in range(1, rang+1):
        yield numero


# Consumiendo el generador
for valor in generador_numeros(rango):
    print(f'Número producido -> {valor}')
