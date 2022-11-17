a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
b = {1, 3, 90, 67, 7, 0}
c = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}

# Unión
union = a | b
print(f"Union a b = {union}")

# Intersección
intersección = a&b
print(f"Intersección a b = {intersección}")

# Diferencia
diferencia = a-b
print(f"Diferencia a b = {diferencia}")

diferencia2 = b-a
print(f"Diferencia b a = {diferencia2}")

# Diferencia Simétrica
simetrica = a^b
print(f"Diferencia simétrica a b = {simetrica}")

# Si a es un subconjunto de b
subconjunto = a.issubset(b)
print(f"¿A es subconjunto de B? = {subconjunto}")

# Si a es un superconunto de b
superconjunto = a.issuperset(b)
print(f"¿A es un superconjunto de B? = {superconjunto}")

# Si a y b son disconexos
print(f"¿A y B son disconexos? = {a.isdisjoint(b)}")
