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

    crear_tabla_citas_sql = """
        CREATE TABLE IF NOT EXISTS citas (
            id_cita INTEGER PRIMARY KEY,
            fecha_cita TEXT NOT NULL,
            paciente_asociado INTEGER NOT NULL,
            FOREIGN KEY (paciente_asociado) REFERENCES paciente (id_paciente)
        );   
    """
    cursor.execute(crear_tabla_citas_sql)
    cursor.close()
