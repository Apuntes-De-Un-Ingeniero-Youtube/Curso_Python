"""
    Crea dos arrays o arreglos unidimensionales que tengan el mismo tamaño (lo pedirá por teclado), 
    en uno de ellos almacenarás nombres de personas como cadenas, en el otro array o arreglo ira almacenando 
    la longitud de los nombres.
"""
tamaño = int(input('Ingrese el tamaño del vector por favor '))
array1 = []
array2 = []

for i in range(tamaño):
    array1.append(input('Ingresa un nombre '))

print(array1)

for x in range(tamaño): # 6 
    array2.append(len(array1[x]))

print(array2)
