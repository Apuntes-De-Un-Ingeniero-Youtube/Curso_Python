"""
Muchos son los cambios que promueven la pandemia generada por el COVID-19
y sus variantes; por mencionar algunos: la alimentación, el control del peso,
etc.  María Fernanda se encuentra preocupada por la salud de su familia, y
encuentra un artículo para llevar un control sobre el peso, conocido como
“índice de masa corporal” (IMC) para adultos de 20 años o más.
El IMC permite establecer una clasificación al relacionar el peso en metros
con el peso en kilogramos; la relación esta determinada por el
peso (kg) / estatura (mts) elevada a la 2, que determina un índice y a su vez
el nivel de peso (bajo peso, normal, sobrepeso y obeso).
"""
edad = int(input('Ingresa tu edad  '))
peso = float(input('Ingresa tu peso en kg  '))
estatura = float(input('Ingresa tu estatura en metros  '))
imc = peso / estatura ** 2

if edad >= 20:
    if 0 <= imc < 18.5:
        print('Bajo peso')
    elif 18.5 <= imc < 25:
        print('normal')
    elif 25 <=  imc < 30:
        print('Sobre peso')
    elif imc >= 30:
        print('Obeso')
    else:
        print('Valores erroneos')
else:
    print('Eres menor de 20 añor, por ende no podemos calcular tu IMC')