from Conexion import Conexion

with Conexion.obtener_conexion_postgres() as conexion:
    with conexion.cursor() as cursor:
        sentencia_sql = """
            UPDATE citas SET MEDICO_ASOCIADO = %s,
                PACIENTE_ASOCIADO = %s,
                FECHA_CITA = %s,
                HORA_CITA = %s
            WHERE ID_CITA = %s 
        """
        # Actualizar un solo registro
        # valores = (3, 2, '2023-01-07', 2.20, 1)
        # cursor.execute(sentencia_sql, valores)

        # Actualizar varios registros
        valores = ((3, 2, '2023-01-07', 2.20, 2),
                   (3, 2, '2023-01-07', 2.20, 3),
                   (3, 2, '2023-01-07', 2.20, 4))

        cursor.executemany(sentencia_sql, valores)
