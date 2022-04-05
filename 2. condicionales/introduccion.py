edad = int(input('Ingresa tu edad  '))
# if (edad >= 18):
#     print('Puedes entrar a la disco ')
# else:
#     print('No puedes entrar a la disco')

# if edad >= 18 and edad < 60:
#     print('eres mayor de edad')
# elif edad >= 60 and edad <= 125:
#     print('perteneces a la tercera edad, eres un abuelito')
# elif edad >= 0 and edad < 18:
#     print('No eres mayor de edad')
# else:
#     print('edad errónea')

if 18 <= edad < 60:
    pass
elif 60 <= edad <= 125:
    print('perteneces a la tercera edad, eres un abuelito')
elif 0 <= edad < 18:
    print('No eres mayor de edad')
else:
    print('edad errónea')
