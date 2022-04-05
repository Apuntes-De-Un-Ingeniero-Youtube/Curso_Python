"""
Pida al usuario la edad y el sexo, para que la computadora le indique si ya puede
jubilarse. Tome en cuenta que un hombre se puede jubilar cuando
tenga 60 años o más, en cambio, una mujer mayor se jubilará si tiene más de 54 años.
"""
edad = int(input('Ingrese su edad  '))
sexo = input('Ingrese su sexo  ')

# if (edad >= 60 and sexo == 'masculino') or (edad >= 54 and sexo == 'femenino'):
#     print('Puedes jubilarte')
# else:
#     print('No puedes jubilarte aún')

print('Puedes jubilarte') if (edad >= 60 and sexo == 'masculino') or (edad >= 54 and sexo == 'femenino') else print('No puedes jubilarte aún')
