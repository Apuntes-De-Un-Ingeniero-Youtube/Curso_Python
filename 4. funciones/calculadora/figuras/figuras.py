import math


def area_perimetro_cuadrado(lado):
    area = lado * lado
    perimetro = 4 * lado
    return area, perimetro


def area_perimetro_rectangulo(base, altura):
    area = base * altura
    perimetro = 2 * (base + altura)
    return area, perimetro


def area_perimetro_circulo(radio):
    area = math.pi * radio * radio
    perimetro = 2 * math.pi * radio
    return area, perimetro


def area_perimetro_hexagono(lado, apotema):
    perimetro = 6 * lado
    area = (perimetro * apotema) / 2
    return area, perimetro


def area_perimetro_triangulo(ladoA, ladoB, ladoC):
    perimetro = ladoA + ladoB + ladoC
    s = perimetro / 2
    area = math.sqrt(s * (s - ladoA) * (s - ladoB) * (s - ladoC))
    return area, perimetro
