from figuras.figuras import *
from figuras.pedir_datos import pedir_datos_figuras


def menu_figuras_geometricas():
    opcion = 0
    while opcion != 6:
        print("\n--------------------------------\n",
              "-  Figuras Geométricas         -\n",
              "--------------------------------\n",
              "-   1. Cuadrado                -\n",
              "-   2. Círculo                 -\n",
              "-   3. Rectángulo              -\n",
              "-   4. Hexagono                -\n",
              "-   5. Triángulo               -\n",
              "-   6. Salir                   -\n",
              "--------------------------------")

        opcion = int(input("Ingrese su opción  "))

        if opcion == 1:
            area, perimetro = area_perimetro_cuadrado(pedir_datos_figuras('cuadrado'))
            print(f'\nArea del cuadrado = {area}\nPerímetro cuadrado = {perimetro}')
        elif opcion == 2:
            area, perimetro = area_perimetro_circulo(pedir_datos_figuras('circulo'))
            print(f'\nArea del circulo = {area}\nPerímetro circulo = {perimetro}')
        elif opcion == 3:
            base, altura = pedir_datos_figuras('rectangulo')
            area, perimetro = area_perimetro_rectangulo(base, altura)
            print(f'\nArea del rectangulo = {area}\nPerímetro rectangulo = {perimetro}')
        elif opcion == 4:
            lado, apotema = pedir_datos_figuras('hexagono')
            area, perimetro = area_perimetro_hexagono(lado, apotema)
            print(f'\nArea del hexagono = {area}\nPerímetro hexagono = {perimetro}')
        elif opcion == 5:
            ladoA, ladoB, ladoC = pedir_datos_figuras('triangulo')
            area, perimetro = area_perimetro_triangulo(ladoA, ladoB, ladoC)
            print(f'\nArea del triangulo = {area}\nPerímetro triangulo = {perimetro}')
        elif opcion == 6:
            print('\n--- Adios ---\n')
        else:
            print('Opción errónea')
