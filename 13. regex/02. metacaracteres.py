import re

lista_nombre = ['Juan Estevez', 'Maria Perez', 'Sandra Lopez', 'Ismel Rojs']

for elemento in lista_nombre:
    if re.findall('^Sandra', elemento):
        print(elemento)

for elemento in lista_nombre:
    if re.findall('Estevez$', elemento, re.IGNORECASE):
        print(elemento)

for elemento in lista_nombre:
    if re.findall('[a-c]', elemento):
        print(elemento)
