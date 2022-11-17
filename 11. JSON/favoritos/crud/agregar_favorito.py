import json


def add_favorito(URL):
    lista = []
    diccionario = {}

    # Solicitar datos al usuario
    titulo = input("\nIngresa el titulo ")
    url = input("Ingresa la URL ")
    comentario = input("Ingresa el comentario")

    # Agregando la URL y el comentario a la lista
    lista.append(url)
    lista.append(comentario)

    # Agregando el favorito al diccionario
    diccionario[titulo] = lista

    escribir_json(URL, diccionario)


def escribir_json(url, datos):
    archivo = open(url, "w")
    json.dump(datos, archivo)
    archivo.close()
