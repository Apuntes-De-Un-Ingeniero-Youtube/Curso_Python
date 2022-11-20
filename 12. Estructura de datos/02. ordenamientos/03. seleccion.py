lista = [4, 2, 5, 1, 7, 8]

for i in range(len(lista)): # i = 0
    minimo = i # 0
    for x in range(i, len(lista)): # x = 1
        if lista[x] < lista[minimo]:
            minimo = x
    aux = lista[i]
    lista[i] = lista[minimo]
    lista[minimo] = aux

print(lista)
