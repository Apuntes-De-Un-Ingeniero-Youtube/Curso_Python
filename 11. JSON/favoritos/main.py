from crud.actualizar_favorito import update_favorito
from crud.agregar_favorito import add_favorito
from crud.eliminar_favorito import delete_favorito
from crud.mostrar_favoritos import view_favoritos

if __name__ == "__main__":
    opc = 0
    URL = "11. JSON/favoritos/favoritos.json"

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
            add_favorito(URL)
        elif opc == 2:
            update_favorito(URL)
        elif opc == 3:
            delete_favorito(URL)
        elif opc == 4:
            view_favoritos(URL)
        elif opc == 5:
            print("Cerrando sesión")
            exit()
        else:
            print("Opción incorrecta")
