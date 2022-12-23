import sqlite3

conexion = sqlite3.connect("./14. bases de datos/sqlite/prueba_sqlite.db")

cursor = conexion.cursor()

crear_tabla_paciente_sql = """
    CREATE TABLE IF NOT EXISTS paciente (
        id_paciente INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        fecha_nacimiento TEXT NOT NULL,
        tipo_identificacion TEXT NOT NULL,
        eps TEXT NOT NULL,
        historia_clinica TEXT NOT NULL
    );
"""

cursor.execute(crear_tabla_paciente_sql)

conexion.commit()

cursor.close()
conexion.close()
