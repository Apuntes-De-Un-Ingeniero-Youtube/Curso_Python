# funciona de manera diferente a map() y filter(). No devuelve una nueva lista basada en el 
# function e iterable hemos pasado. En cambio, devuelve un solo valor.
# Además, en Python 3 reduce() ya no es una función incorporada, y se puede encontrar en el 
# functools módulo.
from functools import reduce

# Ejemplo sin lambdas
def add(x, y):
    return x + y

numeros = [2, 4, 7, 3]
print(reduce(add, numeros))

# utilizando lambdas
numeros = [2, 4, 7, 3]
print(reduce(lambda x,y: x+y, numeros))
print("Con valor inicial: " + str(reduce(lambda x,y: x+y, numeros, 10)))
