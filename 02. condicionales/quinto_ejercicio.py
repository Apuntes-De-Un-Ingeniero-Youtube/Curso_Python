"""
Un almacén de venta de ropa tiene las siguientes promociones para sus clientes,
las cuales consisten en lo siguiente
(pago en efectivo = E, pago con Tarjeta de Crédito = T):

    a. Para ventas menores ó iguales a 100.000, con pago en efectivo,
        se hace un descuento del 20% y si es con tarjeta de crédito, se hace el 10%.
    b. Para ventas mayores a 100.000 y menores o iguales a 200.0000, con pago
        en efectivo, se hace un descuento del 30%, con tarjeta de crédito se hace el 15%.
    c. Para ventas mayores a 200.000, con pago en efectivo, se hace un descuento del 40% y
        con tarjeta de crédito se hace el 20%. Indique el valor del descuento y el
        total a pagar.
"""
pago = int(input("\n------------------------------------------------------------\n"
                 "-     ¿Con qué medio de pago desea realizar su compra?     -\n"
                 "------------------------------------------------------------\n"
                 "-     1. En efectivo                                       -\n"
                 "-     2. Tarjeta de Crédito                                -\n"
                 "------------------------------------------------------------\n"))

if pago == 1:
    compra = float(input("Ingrese el valor de su compra   "))
    descuento1 = compra*0.2
    descuento2 = compra*0.3
    descuento3 = compra*0.4
    if compra >= 0 and compra <= 100000:
        print(f'El descuento efectuado es de: {descuento1}')
        print(f'El total a pagar es: {compra-descuento1}')
    elif compra > 100000 and compra <= 200000:
        print(f'El descuento efectuado es de: {descuento2}')
        print(f'El total a pagar es: {compra-descuento2}')
    elif compra > 200000:
        print(f'El descuento efectuado es de: {descuento3}')
        print(f'El total a pagar es: {compra-descuento3}')
    else:
        print("Valor ingresado incorrecto")
elif pago == 2:
    compra = float(input("Ingrese el valor de su compra   "))
    descuento1 = compra*0.1
    descuento2 = compra*0.15
    descuento3 = compra*0.2
    if compra >= 0 and compra <= 100000:
        print(f'El descuento efectuado es de: {descuento1}')
        print(f'El total a pagar es: {compra-descuento1}')
    elif compra > 100000 and compra <= 200000:
        print(f'El descuento efectuado es de: {descuento2}')
        print(f'El total a pagar es: {compra-descuento2}')
    elif compra > 200000:
        print(f'El descuento efectuado es de: {descuento3}')
        print(f'El total a pagar es: {compra-descuento3}')
    else:
        print("Valor ingresado incorrecto")
else:
    print("Opción incorrecta")
