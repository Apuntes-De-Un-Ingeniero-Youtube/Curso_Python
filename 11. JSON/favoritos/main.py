from agregar_favorito import add_favorito

opcion = 0

while opcion != 5:

    print(f"""
    1. Agregar favorito
    5. Salir
    """)

    opcion = int(input("Ingresa una opción "))

    if opcion == 1:
        add_favorito()
    elif opcion == 5:
        break
