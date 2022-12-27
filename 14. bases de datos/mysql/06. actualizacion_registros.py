from Conexion import Conexion

conexion = Conexion.obtener_conexion_mysql()

# Crear un cursosr para ejecutar consultas
cursor = conexion.cursor()

# Definir el SQL para insertar todos datos en la tabla
insertar_tabla_paciente_sql = """
    UPDATE medico SET nombre = %s,
        tipo_identificacion = %s,
        numero_tarjeta_profesional = %s,
        anios_experiencia = %s,
        especialidad = %s,
        hora_inicio_atencion = %s,
        hora_fin_atencion = %s
    WHERE id_medico = %s
"""

valores = (("Juan Médico update", "CC", "#F7I898", 5.7, "Urología 2", 8.30, 16.25, 899),
           ("Juan Médico update2", "CC 2", "#F7I8 i2", 5.7, "Urología2", 8.45, 18, 345))

# Ejecutar consulta
cursor.executemany(insertar_tabla_paciente_sql, valores)

# Haciendo el commit
conexion.commit()

# Cerrando objetos
cursor.close()
conexion.close()
