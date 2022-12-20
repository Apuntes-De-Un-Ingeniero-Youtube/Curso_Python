import re

fecha = re.compile(
    r'^(?:3[01]|[12][0-9]|0?[1-9])([\-/.])(0?[1-9]|1[1-2])\1\d{4}$')

if fecha.search("03/12/1982"):
    print("Fecha Valida!")
else:
    print("Fecha Invalida!")
