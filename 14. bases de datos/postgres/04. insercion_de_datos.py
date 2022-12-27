from Conexion import Conexion

with Conexion.obtener_conexion_postgres() as conexion:
    with conexion.cursor() as cursor:
        insertar_tabla_citas_sql = """
            INSERT INTO citas (medico_asociado, paciente_asociado, fecha_cita, hora_cita) 
            VALUES (%s,%s,%s,%s)
        """
        valores = (5, 2, "1999/01/07", 12)
        cursor.execute(insertar_tabla_citas_sql, valores)
