import sqlite3

conexion = sqlite3.connect("prueba_sqlite.db")
print(conexion)

conexion.close()
