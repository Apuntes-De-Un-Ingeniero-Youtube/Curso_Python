import sqlite3

conexion = sqlite3.connect("./14. bases de datos/sqlite/prueba_sqlite.db")
print(conexion)

conexion.close()
