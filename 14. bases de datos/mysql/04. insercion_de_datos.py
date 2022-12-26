from Conexion import Conexion

conexion = Conexion.obtener_conexion_mysql()

# Crear un cursosr para ejecutar consultas
cursor = conexion.cursor()

# Definir el SQL para insertar todos datos en la tabla
insertar_tabla_paciente_sql = """
    INSERT INTO medico VALUES (%s,%s,%s,%s,%s,%s,%s,%s);
"""
valores = (77777000, "Juan Médico", "CC", "#F7jhggI8",
           5.7, "Urología", 8.30, 16.25)

# Ejecutar consulta
cursor.execute(insertar_tabla_paciente_sql, valores)

conexion.commit()
cursor.close()
conexion.close()
