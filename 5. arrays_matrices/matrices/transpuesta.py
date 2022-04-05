print('Ingresa el orden de la matriz a calcular ')
filasA, columnasA = int(input()), int(input())  # 4 x 5

# Creando la matriz vacía
matrizA = []
for i in range(filasA):
    matrizA.append([0] * columnasA)

# Rellenando la matriz
print('Ingrese la matriz A')
for fila in range(filasA):
    for columna in range(columnasA):
        matrizA[fila][columna] = float(
            input(f'Ingrese la posición número {fila}, {columna}:  '))

# Matriz Inicial
print('\nMatriz Inicial\n')
for i in matrizA:
    print(i)

filasB = columnasA
columnasB = filasA

# Creando la matriz B vacía
matrizB = []
for i in range(filasB):
    matrizB.append([0] * columnasB)

# Calculando la matriz transpuesta.
for fila in range(filasB):
    for columna in range(columnasB):
        matrizB[fila][columna] = matrizA[columna][fila]

# Matriz Inicial
print('\nMatriz Transpuesta\n')
for i in matrizB:
    print(i)
