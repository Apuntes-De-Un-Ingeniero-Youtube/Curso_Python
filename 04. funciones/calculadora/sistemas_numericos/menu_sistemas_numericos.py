from sistemas_numericos.sistemas_numericos import *


def sistemas_numericos():
    opc = 0
    while opc != 5:
        print(" \n--------------------------------\n",
              "-  ¿Que base desea convertir?  -\n",
              "--------------------------------\n",
              "-   1. Decimal                 -\n",
              "-   2. Binario                 -\n",
              "-   3. Octal                   -\n",
              "-   4. Hexadecimal             -\n",
              "-   5. Salir                   -\n",
              "--------------------------------")
        opc = int(input('Ingrese su opción   '))

        if opc == 1:
            print(decimal())
        elif opc == 2:
            print(binario())
        elif opc == 3:
            print(octal())
        elif opc == 4:
            print(hexadecimal())
        elif opc == 5:
            print('--- Adiós ---')
            exit()
        else:
            print('Opción errónea')
