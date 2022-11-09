from crud.agregar_favorito import add_favorito
from crud.actualizar_favorito import update_favorito
from crud.eliminar_favorito import delete_favorito

opc = 0

while opc != 5:
    print(f"""
    1. Agregar favorito.
    2. Actualizar favorito.
    3. Eliminar favorito.
    4. Consultar favoritos.
    5. Salir
    """)

    opc = int(input("Ingresa la opción "))

    if opc == 1:
        add_favorito()
    elif opc == 2:
        update_favorito()
    elif opc == 3:
        delete_favorito()
    elif opc == 4:
        pass
    elif opc == 5:
        print("Cerrando sesión")
        exit()
    else:
        print("Opción incorrecta")
