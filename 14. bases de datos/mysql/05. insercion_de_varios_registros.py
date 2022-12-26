from Conexion import Conexion

conexion = Conexion.obtener_conexion_mysql()

# Crear un cursosr para ejecutar consultas
cursor = conexion.cursor()

# Definir el SQL para insertar todos datos en la tabla
insertar_tabla_paciente_sql = """
    INSERT INTO medico VALUES (%s,%s,%s,%s,%s,%s,%s,%s);
"""
valores = ((899, "Juan Médico", "CC", "#F7I898", 5.7, "Urología", 8.30, 16.25),
           (345, "Juan Médico 2", "CC 2", "#F7I8 i2", 5.7, "Urología2", 8.30, 16.25))

# Ejecutar consulta
cursor.executemany(insertar_tabla_paciente_sql, valores)

# Haciendo el commit
conexion.commit()

# Cerrando objetos
cursor.close()
conexion.close()
