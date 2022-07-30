# Cree un script en Python el cuál oermita al usuario ingresar diferentes cadenas y
# efectuar un filtro a cada una de esas cadenas para verificar cuales de ellas
# inician con una letra especificada por el usuario
# "cadena1","cadena2","cadena1"
array = input('Ingrese cadenas de texto separadas por comas y sin espacios ')
array_sin_repetidos = list(set(array.split(',')))
delimitador = input('Ingrese la condición de inicio de las cadenas ')
resultado = filter(lambda x: str(x).startswith(delimitador), array_sin_repetidos)
print(sorted(list(resultado)))
