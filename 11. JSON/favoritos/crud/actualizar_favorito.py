import json


def update_favorito():
    lista = []

    # Solicitando el favorito a modificar
    titulo_modificar = input("Ingrese el título a modificar ")

    archivo = open("11. JSON/favoritos/favoritos.json", "r")
    datos = json.load(archivo)
    archivo.close()

    # Eliminando el favorito.
    if titulo_modificar in datos:
        del datos[titulo_modificar]
    else:
        print("No existe el favorito en el archivo")

    # Escribiendo en el archivo.json
    archivo = open("11. JSON/favoritos/favoritos.json", "w")
    json.dump(datos, archivo)
    archivo.close()

    # Solicitando los datos a modificar
    nuevo_titulo = input("Ingresa el n8evo tpitulo ")
    nueva_url = input("Ingresa la nueva URL ")
    nuevo_comentario = input("Ingresa el nuevo comentario ")

    # Agregando el nuevo comentario y la nueva URL a la lista
    lista.append(nueva_url)
    lista.append(nuevo_comentario)

    archivo = open("11. JSON/favoritos/favoritos.json", "r")
    datos = json.load(archivo)
    archivo.close()

    # Agregando el favorito al diccionario
    datos[nuevo_titulo] = lista

    # Escribiendo en el archivo.json
    archivo = open("11. JSON/favoritos/favoritos.json", "w")
    json.dump(datos, archivo)
    archivo.close()


