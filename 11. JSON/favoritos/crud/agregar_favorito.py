import json


def add_favorito():
    lista = []
    diccionario = {}

    # Solicitar datos al usuario
    titulo = input("\nIngresa el titulo ")
    url = input("Ingresa la URL ")
    comentario = input("Ingresa el comentario")

    # Agregando la URL y el comentario a la lista
    lista.append(url)
    lista.append(comentario)

    archivo = open("11. JSON/favoritos/favoritos.json", "w")

    # Agregando el favorito al diccionario
    diccionario[titulo] = lista

    # Escribiendo el favorito en el archivo .json
    json.dump(diccionario, archivo)
    archivo.close()


add_favorito()
