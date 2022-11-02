import os

# Eliminando ficheros o archivos
if os.path.exists('prueba.txt'):
    os.remove('prueba.txt')
else:
    print('El archivo que intenta eliminar no existe.')

# Eliminando carpetas
os.rmdir("prueba basura")
