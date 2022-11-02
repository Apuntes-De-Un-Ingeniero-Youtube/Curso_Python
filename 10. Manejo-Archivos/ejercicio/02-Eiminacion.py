import os

# Creando fichero de texto con la conversación.
try:
    archivo = open("frase.txt", "at", encoding="utf-8")
    frase = input('Ingresa una frase ')
    palabra = input('Ingresa la palabra a evaluar ')
    if (frase.__contains__(palabra)):
        archivo.close()
        # Eliminando ficheros o archivos
        if os.path.exists('frase.txt'):
            os.remove('frase.txt')
        else:
            print('El archivo que intenta eliminar no existe.')
    else:
        archivo.write(frase + "\n")
except Exception as e:
    print(e)
finally:
    archivo.close()
