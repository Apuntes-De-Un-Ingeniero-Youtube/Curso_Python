"""
    Crear un algoritmo que muestre los primeros 10 números de la 
    sucesión de Fibonacci. La sucesión comienza con los 
    números 0 y 1 y, a partir de éstos, cada elemento es la suma de 
    los dos números anteriores en la secuencia: 
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…
"""
numero = int(input("Hasta donde desea generar la secusión de Fibonacci  ")) #11
n1 = 0 # 3
n2 = 1 # 5
print(n1, n2, end=" ") # 0
 
 # 0, 1, 1, 2, 3, 5

for i in range(numero - 2): # 5
    n3 = n1 + n2 
    print(n3, end=" ") # 5
    n1 = n2 
    n2 = n3