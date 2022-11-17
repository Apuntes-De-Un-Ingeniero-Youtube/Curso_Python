import json


def delete_favorito(URL):
    titulo = input("Ingresa el título del favorito a eliminar ")
    datos = cargar_json(URL)

    if titulo in datos:
        del datos[titulo]
        print("Favorito eliminado")
    else:
        print("No existe el favorito en el archivo")

    escribir_json(URL, datos)


def cargar_json(url):
    archivo = open(url, "r")
    datos = json.load(archivo)
    archivo.close()
    return datos


def escribir_json(url, datos):
    archivo = open(url, "w")
    json.dump(datos, archivo)
    archivo.close()
