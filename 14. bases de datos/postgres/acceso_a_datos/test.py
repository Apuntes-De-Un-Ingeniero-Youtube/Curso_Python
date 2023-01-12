from Cliente import Cliente
from ClienteDAO import ClienteDAO


def solicitar_datos(razon=True):
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    email = input("Email: ")
    telefono = int(input("Telefono: "))
    razon_social = ""
    if razon:
        razon_social = input("Razón social: ")

    return Cliente(nombre, apellido, email, razon_social, telefono)


def consultar_cliente_por_razon_social():
    razon_social = input("Ingresa la razón social ")
    return ClienteDAO.consultar_por_razon_social(razon_social)


if __name__ == "__main__":

    opc = 0

    while opc != 6:

        print(f"""
        1. Agregar Cliente.
        2. Actualizar Cliente.
        3. Eliminar Cliente.
        4. Consultar Cliente por RAZON SOCIAL.
        5. Consultar listado de clientes.
        6. Salir
        """)

        opc = int(input("Ingresa la opción "))

        if opc == 1:
            cliente = solicitar_datos(True)
            filas_afectadas = ClienteDAO.insertar(cliente)
            print(f"Ha sido insertados {filas_afectadas} registros.")
        elif opc == 2:
            cliente_obtenido = consultar_cliente_por_razon_social()

            if cliente_obtenido != -1:
                cliente_actualizar = solicitar_datos(False)
                filas_afectadas = ClienteDAO.actualizar(
                    cliente_actualizar, cliente_obtenido.get_razon_social())
                print(f"Se han modificado {filas_afectadas} registros.")
            else:
                print("El registro que trata de actualizar NO existe en el Sistema.")
        elif opc == 3:
            cliente_eliminar = consultar_cliente_por_razon_social()
            if cliente_eliminar != -1:
                filas_afectadas = ClienteDAO.eliminar(cliente_eliminar)
                print(f"Han sido eliminados {filas_afectadas} registros.")
            else:
                print("El registro que trata de eliminar NO existe en el Sistema.")
        elif opc == 4:
            cliente_obtenido = consultar_cliente_por_razon_social()
            if cliente_obtenido != -1:
                print(cliente_obtenido)
            else:
                print("Registro NO encontrado")
            if cliente_obtenido == 0:
                print("Ocurrió un error inesperado")
        elif opc == 5:
            clientes_obtenido = ClienteDAO.seleccionar()
            for cliente in clientes_obtenido:
                print(cliente, end="\n---------------------\n")
        elif opc == 6:
            break
