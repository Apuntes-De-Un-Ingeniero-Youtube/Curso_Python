from Conexion import Conexion

conexion = Conexion.obtener_conexion_mysql()
# Crear un cursosr para ejecutar consultas
cursor = conexion.cursor()

# Definir el SQL para crear la tabla
eliminar_tabla_paciente_sql = """
    DROP TABLE IF EXISTS medico;
"""

# Ejecutar consulta
cursor.execute(eliminar_tabla_paciente_sql)

# Haciendo el commit
conexion.commit()

# Cerrando objetos
cursor.close()
conexion.close()
