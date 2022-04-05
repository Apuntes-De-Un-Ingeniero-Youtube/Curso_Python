print('Ingresa el orden de la matriz a calcular ')
filasA, columnasA = int(input()), int(input()) # 4 x 4

diagonal = 0

if filasA == columnasA:

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

    # Calculando la diagonal principal de la matriz A
    for fila in range(filasA):
        for columna in range(columnasA):
            if fila == columna:
                diagonal += matrizA[fila][columna]
    
    print(f'El valor de la diagonal principal es: {diagonal}')
