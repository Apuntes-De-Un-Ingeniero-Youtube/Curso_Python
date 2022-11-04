"""
    Crear un programa python que simule una máquina registradora, 
    la cual al ingresar una cantidad de dinero a pagar, deberá entregar 
    los vueltos únicamente en  billetes de 500, 100, 50, 10, 1 
    respectivamente.
"""
# Para saber cuantas billetes tene,os de cada denominación
contador_quinientos = 0
contador_cien = 0
contador_cincuenta = 0
contador_diez = 0
contador_uno = 0

total_pago = float(input("Ingrese el total a pagar en el parqueadero  "))  # 27520
pago_cliente = float(input("Ingrese el pago por favor  "))  # 30000
devolucion = pago_cliente-total_pago  # 2480

if pago_cliente < total_pago:
    print('Dinero insuficiente')
else:
    contador_quinientos = int(devolucion/500)  # 4 
    aux = devolucion - (500 * contador_quinientos)  # 480
    contador_cien = int(aux/100) # 4
    aux2 = aux - (100 * contador_cien) # 80
    contador_cincuenta = int(aux2 / 50) # 1
    aux3 = aux2 - (50 * contador_cincuenta) # 30
    contador_diez = int(aux3 / 10) # 3
    aux4 = aux3 - (10 * contador_diez) # 0
    contador_uno = int(aux4 / 1) # 0

    print('\nSu cambio es de ', devolucion, ' y se entregará de la siguiente manera',
          '\nBilletes de 500              ', contador_quinientos,
          '\nBilletes de 100              ', contador_cien,
          '\nBilletes de 50               ', contador_cincuenta,
          '\nBilletes de 10               ', contador_diez,
          '\nBilletes de 1                ', contador_uno)

