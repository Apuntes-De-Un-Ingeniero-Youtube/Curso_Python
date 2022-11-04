def pedir_datos_figuras(figura):
    if figura == 'cuadrado':
        lado = float(input('\nIngrese el lado de la figura  '))
        return lado
    elif figura == 'rectangulo':
        base = float(input('\nIngrese la base de la figura '))
        altura = float(input('Ingrese la altura de la figura '))
        return base, altura
    elif figura == 'circulo':
        radio = float(input('\nIngrese el radio del círculo  '))
        return radio
    elif figura == 'hexagono':
        lado = float(input('\nIngrese el lado de la figura  '))
        apotema = float(input('Ingrese el apotema de la figura  '))
        return lado, apotema
    elif figura == 'triangulo':
        ladoA = float(input('\nIngrese el lado A  '))
        ladoB = float(input('Ingrese el lado B  '))
        ladoC = float(input('Ingrese el lado C  '))
        return ladoA, ladoB, ladoC