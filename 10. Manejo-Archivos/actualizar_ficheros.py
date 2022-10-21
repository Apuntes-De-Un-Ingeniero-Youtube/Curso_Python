try:
    archivo = open('prueba.txt', 'a', encoding='utf-8')
    archivo.write(
        "\nesta se supone que debería ser la tercera línea de nuestro fichero de texto.")
except Exception as e:
    print(e)
finally:
    archivo.close()
