# Lista de listas
lista_listas = [[1,2,3],[4,5,6],[7,8,9]]
# Convertimos la lista de listas en una sola lista
lista_simple = [valor for sublista in lista_listas for valor in sublista]
print(f'lista simple: {lista_simple}')

# Ahora creamos una lista de numeros pares a partir de la lista_listas
# Sin list comprehensions, ciclos for anidados
lista_pares = []
for sublista in lista_listas:
    for valor in sublista:
        if valor%2==0:
            lista_pares.append(valor)
print(f'Lista pares: {lista_pares}')

# Con list comprehensions, en una sola línea de código
# No es necesario separar las líneas, solo es para mejor lectura de código
lista_pares = [valor for sublista in lista_listas for valor in sublista if valor%2==0]
print(f'Lista pares: {lista_pares}')