matriz3x3 = [[1,2,3],
             [4,5,6],
             [7,8,9]]

# punto = matriz3x3[1][2]

# print(punto)
# print(matriz3x3[2][0])

# Sumar los elementos de la matriz
suma = 0
for i in range(len(matriz3x3)): # 2
    for j in range(len(matriz3x3)): # 2
        suma += matriz3x3[i][j] # 45

print(suma)