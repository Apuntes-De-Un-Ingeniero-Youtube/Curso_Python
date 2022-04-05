import numpy as np

#filas = int(input('Ingrese el número de filas de las matrices '))  # 3
#columnas = int(input('\nIngrese el número de columnas de las matrices '))  # 6


def crear_matriz(filas, columnas):
    f = -1; c = -1
    e_fil = []
    for i in range(0, filas):  # 3
        e_col = []
        f += 1
        for j in range(0, columnas):
            c += 1
            valor = int(input(f'Ingrese el valor del componente {i},{j} => '))
            e_col.append(valor)
        e_fil.append(e_col)
    return e_fil


#matrizA = np.array(crear_matriz(filas, columnas))
#matrizB = np.array(crear_matriz(filas, columnas))

#suma = matrizA + matrizB
#resta = matrizA - matrizB
#multiplicacion = matrizA * matrizB

#print(f"Suma de matrices: \n{suma} \n\n Resta de matrices: \n{resta} \n\n Multiplicación de matrices: \n{multiplicacion}")

def multiplicar_matrices(matrizA, matrizB):
    if len(matrizA[0]) == len(matrizB):
        # creando las dimensiones de la matriz resultante
        matrizC = []
        for i in range(len(matrizA)):
            matrizC.append([])
            for j in range(len(matrizB[0])):
                matrizC[i].append(0)

        # multiplicación
        for i in range(len(matrizA)):
            for j in range(len(matrizB[0])):
                for k in range(len(matrizA[0])):
                    matrizC[i][j] += matrizA[i][k] * matrizB[k][j]

        return matrizC
    else:
        return None

multiplicacion2 = multiplicar_matrices(crear_matriz(2, 3), crear_matriz(3, 2))

if multiplicacion2 == None:
    print('no se puede')
else:
    for fila in multiplicacion2:
        print('[', end=" ")
        for elemento in fila:
            print(elemento, end=" ")
        print(']')