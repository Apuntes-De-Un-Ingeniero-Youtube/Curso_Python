import sqlite3

conexion = sqlite3.connect("./14. bases de datos/sqlite/prueba_sqlite.db")

cursor = conexion.cursor()

eliminar_tabla_paciente_sql = """
    DROP TABLE IF EXISTS paciente;
"""

cursor.execute(eliminar_tabla_paciente_sql)

conexion.commit()

cursor.close()
conexion.close()
