import json


def update_favorito(URL):
    lista = []

    # Solicitando el favorito a modificar
    titulo_modificar = input("Ingrese el título a modificar ")

    datos = cargar_json(URL)

    # Eliminando el favorito.
    if titulo_modificar in datos:
        del datos[titulo_modificar]

        # Escribiendo en el archivo.json
        escribir_json(URL, datos)

        # Solicitando los datos a modificar
        nuevo_titulo = input("Ingresa el nuevo título ")
        nueva_url = input("Ingresa la nueva URL ")
        nuevo_comentario = input("Ingresa el nuevo comentario ")

        # Agregando el nuevo comentario y la nueva URL a la lista
        lista.append(nueva_url)
        lista.append(nuevo_comentario)

        datos = cargar_json(URL)

        # Agregando el favorito al diccionario
        datos[nuevo_titulo] = lista

        # Escribiendo en el archivo.json
        escribir_json(URL, datos)

    else:
        print("No existe el favorito en el archivo")


def escribir_json(url, datos):
    archivo = open(url, "w")
    json.dump(datos, archivo)
    archivo.close()


def cargar_json(url):
    archivo = open(url, "r")
    datos = json.load(archivo)
    archivo.close()
    return datos
