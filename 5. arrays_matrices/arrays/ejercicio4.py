"""
    Diseñe un programa que lea un vector y calcule si hay un numero que
    sea igual a la suma de los demas elementos del vector
"""
vector = []
tamaño = int(input('Ingrese el tamaño del vector '))
suma = 0 
numeroSuma = -1

# Rellenando vector
for i in range(tamaño):
    numero = int(input('Ingrese un número ')) 
    vector.append(numero)
    suma += vector[i]

    if vector[i] == suma:
        numeroSuma = suma

if numeroSuma != -1:
    print(f'El número {numeroSuma} es la suma de los demás números del vector')
else:
    print('Ningún número cumple con el criterio')