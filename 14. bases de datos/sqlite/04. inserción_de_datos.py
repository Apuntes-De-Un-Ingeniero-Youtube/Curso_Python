import sqlite3

conexion = sqlite3.connect("./14. bases de datos/sqlite/prueba_sqlite.db")

cursor = conexion.cursor()

insertar_tabla_paciente_sql = """
    INSERT INTO paciente (
            id_paciente, 
            nombre, 
            fecha_nacimiento, 
            tipo_identificacion, 
            eps, 
            historia_clinica) 
        VALUES ($s, $s, $s, $s, $s, $s);
"""

valores = (1, "Juan Estevez", "2001/05/01", "CC", "EPS 1", "Sufre de algo")

cursor.execute(insertar_tabla_paciente_sql, valores)

conexion.commit()

cursor.close()
conexion.close()
