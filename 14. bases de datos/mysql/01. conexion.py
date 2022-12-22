import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    db="prueba_mysql")

print(conexion)

conexion.close()
