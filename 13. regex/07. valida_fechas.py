import re

fecha = re.compile(r'^(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[012])/((19|20)dd)$')

if fecha.search("13/02/1982"):
    print("Fecha Valida!")
else:
    print("Fecha Invalida!")
