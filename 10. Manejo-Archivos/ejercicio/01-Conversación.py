# Creando fichero de texto con la conversación.
try:
    archivo = open("conversación.txt", "wt", encoding="utf-8")
    archivo.write(
        "Hola\nHola, ¿Cómo estás?\nNo muy bien y ¿tú?\nPerro\nOk, hablamos mañana.\nAdiós.")
except Exception as e:
    print(e)
finally:
    archivo.close()

# Buscando la palabra o frase a reemplazar
try:
    archivo = open("conversación.txt", "rt", encoding="utf-8")
    reemplazo = ""

    for linea in archivo:
        linea = linea.strip()
        cambio = linea.replace("Perro", "Podría estar mejor")
        reemplazo = reemplazo + cambio + "\n"
except Exception as ex:
    print(ex)
finally:
    archivo.close()

# Reemplazar la frase en el fichero original
try:
    archivo = open("conversación.txt", "wt", encoding="utf-8")
    archivo.write(reemplazo)
except Exception as exx:
    print(exx)
finally:
    archivo.close()
