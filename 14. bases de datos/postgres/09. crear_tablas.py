from Conexion import Conexion

with Conexion.obtener_conexion_postgres() as conexion:
    with conexion.cursor() as cursor:
        crear_tabla_medico_sql = """
            CREATE TABLE IF NOT EXISTS medico (
                id_medico SERIAL PRIMARY KEY,
                nombre_medico VARCHAR(50) NOT NULL,
                especialidad VARCHAR(50) NOT NULL
            ) 
        """
        crear_tabla_citas_sql = """
            CREATE TABLE IF NOT EXISTS citas (
                id_cita SERIAL PRIMARY KEY,
                medico_asociado INTEGER NOT NULL,
                paciente_asociado INTEGER NOT NULL,
                fecha_cita DATE,
                hora_cita DECIMAL(4, 2),
                FOREIGN KEY (medico_asociado) REFERENCES medico(id_medico)
            ) 
        """
        cursor.execute(crear_tabla_citas_sql)
