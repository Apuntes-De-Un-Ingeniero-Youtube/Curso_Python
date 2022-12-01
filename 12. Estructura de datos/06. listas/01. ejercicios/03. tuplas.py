"""
    Cree una tupla con los meses del año, pide números al usuario, si el número esta entre
    1 y la longitud máxima de la tupla, muestre el contenido de esa posición, si no, muestre
    un mensaje de error

    El programa debe terminar cuando el usuario presione el 0
"""
meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
         "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")


def funcion():
    opcion = None

    while opcion != 0:
        try:
            numero = int(
                input(f"Ingresa un número entre 0 y {len(meses)} con 0 para salir "))
            if 1 <= numero <= len(meses):
                print(meses[numero - 1])
            elif numero == 0:
                print("Adiós".center(50, "-"))
                opcion = 0
            else:
                print("Opción incorrecta vuelve a intentarlo")
                funcion()
        except Exception as e:
            print(e)
            print("Ha ocurrido un error inesparado vuelve a intentarlo")
            break


funcion()
