"""
    Crear un diccionario que permita almacenar n artículos, utilizar como clave el
    nombre del producto y como valor el precio del mismo.

    Imprimir de manera completa el diccionario
    Imprimir sólo los artículos que superen los $100
"""


def menu():
    opc = 0
    diccionario = {}
    try:
        while opc != 4:
            print("\nDiccionario Artículos\n"
                  + "\n\t1. Ingresar artículo"
                  + "\n\t2. Mostrar todos los productos"
                  + "\n\t3. Productos mayores a 100"
                  + "\n\t4. Salir")
            opc = int(input("Ingrese su opción "))

            if opc == 1:
                ingresar_articulo(diccionario)
            elif opc == 2:
                print(diccionario)
            elif opc == 3:
                mostrar_precios_mayor_100(diccionario)
            elif opc == 4:
                print(" Adiós ".center(50, "-"))
            else:
                print("Ingresaste una opción errónea")
    except Exception as e:
        print("\n Solo se permiten caracteres numéricos")
        print(e)


def ingresar_articulo(diccionario):
    nombre_articulo = input("Ingrese el nombre del artículo ")
    precio = float(input("Ingrese el precio del artículo "))
    diccionario[nombre_articulo] = precio


def mostrar_precios_mayor_100(diccionario):
    for i in diccionario:
        if diccionario[i] > 100:
            print(diccionario[i])


menu()
