from Conexion import Conexion

with Conexion.obtener_conexion_postgres() as conexion:
    with conexion.cursor() as cursor:
        sentencia_sql = """
            SELECT citas.fecha_cita, citas.hora_cita, medico.nombre_medico, medico.especialidad
            FROM citas INNER JOIN medico ON citas.medico_asociado = medico.id_medico 
            WHERE id_medico = 1
        """
        cursor.execute(sentencia_sql)
        registro = cursor.fetchone()
        print(registro)
