from Conexion import Conexion

with Conexion.obtener_conexion_postgres() as conexion:
    with conexion.cursor() as cursor:
        crear_tabla_citas_sql = """
            CREATE TABLE IF NOT EXISTS citas (
                id_cita SERIAL PRIMARY KEY,
                medico_asociado INTEGER NOT NULL,
                paciente_asociado INTEGER NOT NULL,
                fecha_cita DATE,
                hora_cita DECIMAL(4, 2)
            )
        """
        cursor.execute(crear_tabla_citas_sql)
