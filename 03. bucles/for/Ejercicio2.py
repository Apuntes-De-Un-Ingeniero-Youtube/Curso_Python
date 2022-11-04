"""
    Realizar un programa python que sea capaz de imprimir la tabla de
    multiplicar de cualquier número ingresado por pantalla.
"""
# import math
numero = int(input("Ingresa el número del cual deseas la tabla de multiplicar  ")) # 5

for i in range(5, 25, 3): # 8
    # print(f'{numero} x {i} = {math.floor(numero * i)}') # 5 x 8 = 40
    print(f'{numero} x {i} = {numero * i}') # 5 x 8 = 40