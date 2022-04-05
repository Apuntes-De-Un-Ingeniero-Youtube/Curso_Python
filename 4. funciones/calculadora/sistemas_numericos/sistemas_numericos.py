def decimal():
    decimal = int(input('\nIngrese un número decimal (Base 10)  '))
    binario = bin(decimal)
    octal = oct(decimal)
    hexadecimal = hex(decimal)
    return f'''
        Decimal - Binario      =   {binario}
        Decimal - Octal        =   {octal}
        Decimal - Hexadecimal  =   {hexadecimal}
    '''

def binario():
    binario = input('\nIngrese un número binario (Base 2)  ')
    decimal = int(binario, base=2)
    octal = oct(decimal)
    hexadecimal = hex(decimal)
    return f'''
        Binario - Decimal       =   {decimal}
        Binario - Octal         =   {octal}
        Binario - Hexadecimal   =   {hexadecimal}
    '''

def octal():
    octal = input('\nIngrese un número octal (Base 8)  ')
    decimal = int(octal, base=8)
    binario = bin(decimal)
    hexadecimal = hex(decimal)
    return f'''
        Octal - Decimal       =   {decimal}
        Octal - Binario       =   {binario}
        Octal - Hexadecimal   =   {hexadecimal}
    '''

def hexadecimal():
    hexadecimal = input('\nIngrese un número hexadecimal (Base 16)  ')
    decimal = int(hexadecimal, base=16)
    octal = oct(decimal)
    binario = bin(decimal)
    return f'''
        hexadecimal - Decimal       =   {decimal}
        hexadecimal - Octal         =   {octal}
        hexadecimal - binario       =   {binario}
    '''