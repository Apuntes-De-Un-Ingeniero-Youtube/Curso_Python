from Conexion import Conexion

with Conexion.obtener_conexion_sqlite() as conexion:
    cursor = conexion.cursor()
    eliminar_tabla_paciente_sql = """
        DROP TABLE IF EXISTS paciente;
    """
    cursor.execute(eliminar_tabla_paciente_sql)
    cursor.close()
