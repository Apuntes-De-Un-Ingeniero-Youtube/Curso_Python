import json
import os


def add_favorito():
    lista = []
    diccionario = {}

    # Solicitando datos
    titulo = input("\nIngresa el título ")
    url = input("Ingresa la URL ")
    comentario = input("Ingresa el comentario ")

    # Añadiendo la URL y el comentario a la lista
    lista.append(url)
    lista.append(comentario)

    # Abriendo el archivo.json en modo escritura
    filename = r"11. JSON/favoritos/favoritos.json"
    if os.path.isfile(filename):
        archivo = open("favoritos.json", "r")
        datos = json.load(archivo)
        archivo.close()

        # Añadiendo el favorito al diccionario
        
        datos[titulo] = lista

        # Escribiendo en el archivo
        archivo = open("favoritos.json", "w")
        json.dump(datos, archivo)
        archivo.close()
    else:
        archivo = open("favoritos.json", "w")

        # Añadiendo el favorito al diccionario
        diccionario[titulo] = lista

        # Escribiendo el favorito en el archivo
        json.dump(diccionario, archivo)
        archivo.close()
