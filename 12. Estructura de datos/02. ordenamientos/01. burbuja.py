lista = [100, 50, 20, 10, 8, 4, 2]

for i in range(len(lista)):  # Evalúa las pasadas
    for x in range(len(lista) - 1):  # Evalua los elementos en cada pasada
        if lista[x] > lista[x + 1]:
            aux = lista[x] # 100
            lista[x] = lista[x + 1] # 50 20 10 20 50 100
            lista[x + 1] = aux 
        print(lista)

print(lista)
