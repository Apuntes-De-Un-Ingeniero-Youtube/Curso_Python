from operaciones_basicas.menu_operaciones_basicas import operaciones_basicas
from sistemas_numericos.menu_sistemas_numericos import *
from figuras.menu_figuras_geometricas import menu_figuras_geometricas

opcion = 0

while opcion != 3:
    print("\n ---------------------------\n",
          "-       CALCULADORA         -\n",
          "-----------------------------\n",
          "-   1. Operaciones Básicas  -\n",
          "-   2. Sistemas numéricos   -\n",
          "-   3. Figuras Geométricas  -\n",
          "-   4. Salir                -\n",
          "-----------------------------")

    opcion = int(input('Ingrese su opción  '))

    if opcion == 1:
        print(operaciones_basicas())
    elif opcion == 2:
        sistemas_numericos()
    elif opcion == 3:
        menu_figuras_geometricas()
    elif opcion == 4:
        print('\n--- Adios ---\n')
        exit()
    else:
        print('Opción erronea')
