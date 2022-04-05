print('Ingrese el orden de la matriz A')
filasA, columnasA = int(input()), int(input())  # 2 x 3

print('Ingrese el orden de la matriz B')
filasB, columnasB = int(input()), int(input())  # 3 x 2

# Si es posible o no hacer la multiplicación
if columnasA == filasB:

    # Crear la matriz A con el tamaño filasA * columnasA
    matrizA = []
    for i in range(filasA):
        matrizA.append([0] * columnasA)

    # Crear la matriz B con el tamaño filasB * columnasB
    matrizB = []
    for i in range(filasB):
        matrizB.append([0] * columnasB)

    # Rellenando la matriz A
    print('Ingrese la matriz A ')
    for filas in range(filasA):  # 1 -> 2
        for columnas in range(columnasA):  # 2 -> 3
            matrizA[filas][columnas] = float(
                input(f'Ingresa la posición número {filas},{columnas} se la matriz A '))

    # Rellenando la matriz B
    print('Ingrese la matriz B ')
    for filas in range(filasB):  # 1 -> 2
        for columnas in range(columnasB):  # 2 -> 3
            matrizB[filas][columnas] = float(
                input(f'Ingresa la posición número {filas},{columnas} se la matriz B '))

    # Creando la matriz resultante de tamaño filasA * columnasB
    matrizC = []
    for i in range(filasA):
        matrizC.append([0] * columnasB)

    # Efectuando la multiplicación entre las matrices A y B
    for i in range(len(matrizA)):  # Recorre las filas
        for j in range(len(matrizB[0])):  # Recorre las columnas
            for k in range(len(matrizB)):
                matrizC[i][j] += matrizA[i][k] * matrizB[k][j]

    # Mostrar la matriz resultante
    print('\nLa matriz resultante es: ')
    for i in matrizC:
        print(i)

else:
    print('No se puede efectuar la multiplicación')
