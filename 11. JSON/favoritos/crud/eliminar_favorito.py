import json


def delete_favorito():

    titulo = input("Ingresa el título del favorito a eliminar ")

    archivo = open("11. JSON/favoritos/favoritos.json", "r")
    datos = json.load(archivo)
    archivo.close()

    if titulo in datos:
        del datos[titulo]
        print("Favorito eliminado")
    else:
        print("No existe el favorito en el archivo")

    archivo = open("11. JSON/favoritos/favoritos.json", "w")
    json.dump(datos, archivo)
    archivo.close()

