import re

# Uno de los usos que más se le dan a las expresiones regulares
# es la verificación de correos electronicos
patron = re.compile(r"[w.%+-]+@[w.-]+.[a-zA-Z]{2,6}")

# Comprobemos sí este es un correo electronico valido
if patron.search("pythondi1io@gmail.com"):
    print("Correo valido!")
else:
    print("Correo Invalido!")
