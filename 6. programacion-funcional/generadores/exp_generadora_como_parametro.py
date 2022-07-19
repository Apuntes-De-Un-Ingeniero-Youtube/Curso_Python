# Podemos pasar una expresión generadora como parámetro a una función
rango = int(input('Ingrese un número por favor '))  # 4
suma = sum(numero * numero for numero in range(rango))  # 0 + 1 + 4 + 9 = 14
print(f'Resultado de la suma -> {suma}')
