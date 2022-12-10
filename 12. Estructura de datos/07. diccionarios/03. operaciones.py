from pprint import pprint as pp
diccionario = {"Nombre": "Juan Carlos"}

# Método get recupera una llave y en caso de que no exista no lanza excepciones
# además, podemos regresar un valor en caso de que no exista la llave
print(diccionario.get("Nombre", "No se encontró la llave"))

# setDefault el cual modifica el diccionario, ademas se agrega un valor por defecto
apellido = diccionario.setdefault("Apellido", "Estevez")
print(apellido)
print(diccionario)

# Imprimiendo con pprint
pp(diccionario, sort_dicts=False)

# Imprimiendo con for
for valor in diccionario.values():
    print(valor)

for key in diccionario.keys():
    print(key)

for key, value in diccionario.items():
    print(key, value)

print("\n\n".center(50, "-"))

d = {"uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5}
print(d)

# Eliminar un valor del diccionario
d.pop("dos")
print(d)

# Eliminar elementos con popItem() elimina el último valor
d.popitem()
print(d)

# Eliminar con del
del d["tres"]
print(d)

# Consultar el tamaño del diccionario
print(len(d))

# Eliminar el diccionario por completo
d.clear()
print(d)
