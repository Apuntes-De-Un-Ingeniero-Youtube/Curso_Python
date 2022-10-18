try:
    archivo = open('prueba.txt', 'w', encoding="utf-8");
    archivo.write('Agregamos una línea de texto directamente desde Python\n')
    archivo.write('hola')
except Exception as e:
    print(e)
finally:
    archivo.close()