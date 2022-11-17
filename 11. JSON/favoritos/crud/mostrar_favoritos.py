import json


def view_favoritos(URL):
    datos = cargar_json(URL)

    print("\n--- Listado de Favoritos ---\n")
    for favorito in datos:
        print(f"{favorito} = {datos[favorito]}")


def cargar_json(url):
    archivo = open(url, "r")
    datos = json.load(archivo)
    archivo.close()
    return datos
