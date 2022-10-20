try:
    archivo = open("prueba.txt", "rt", encoding='utf-8')

    # Imprimiendo todo el archivo
    print(archivo.read())

    # Imprimiendo solo algunos caracteres
    print(archivo.read(7))

    # Imprimiendo líneas completas
    print(archivo.readline())

    # Imprimiendo todas las líneas del archivo
    for linea in archivo:
        print(linea, end="")
except Exception as e:
    print(e)
finally:
    archivo.close()
