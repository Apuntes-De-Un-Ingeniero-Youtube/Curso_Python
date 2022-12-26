from Conexion import Conexion

with Conexion.obtener_conexion_sqlite() as conexion:
    cursor = conexion.cursor()

    insertar_tabla_paciente_sql = """
        INSERT INTO paciente (
                id_paciente, 
                nombre, 
                fecha_nacimiento, 
                tipo_identificacion, 
                eps, 
                historia_clinica) 
            VALUES (?, ?, ?, ?, ?, ?);
    """
    valores = (3, "Juan Estevez", "2001/05/01",
               "CC", "EPS 1", "Sufre de algo")

    cursor.execute(insertar_tabla_paciente_sql, valores)
    cursor.close()
