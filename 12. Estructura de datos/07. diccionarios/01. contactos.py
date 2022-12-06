"""
    Cree un diccionario donde la clave sea el nombre del usuario y el 
    valor sea el telefono
"""
diccionario = {}
opcion = 1

try:
    while opcion == 1:
        nombre = input("Ingrese el nombre por favor ")
        telefono = int(input("Ingrese el teléfono "))
        diccionario[nombre] = telefono
        opcion = int(
            input("Digite 1 para agregar mas contactos o 0 para salir "))
    print(diccionario.keys())
except Exception as e:
    print("Ocurrió un error " + e)
