from Conexion import Conexion

with Conexion.obtener_conexion_sqlite() as conexion:
    cursor = conexion.cursor()
    crear_tabla_paciente_sql = """
        CREATE TABLE IF NOT EXISTS paciente (
            id_paciente INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            fecha_nacimiento TEXT NOT NULL,
            tipo_identificacion TEXT NOT NULL,
            eps TEXT NOT NULL,
            historia_clinica TEXT NOT NULL
        );
    """
    cursor.execute(crear_tabla_paciente_sql)
    cursor.close()
