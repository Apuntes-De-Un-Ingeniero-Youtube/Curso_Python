import re

nombre1 = 'Juan Estevez'
nombre2 = 'Maria Arciniegas'

print('Nombre encontrado'if re.match(
    'JuA.', nombre1, re.IGNORECASE) else 'Nombre NO encontrado')

print('Apellido encontrado'if re.search('.ni', nombre2,
      re.IGNORECASE) else 'Apellido NO encontrado')
