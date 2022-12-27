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
    valores = [
        (111, "Juan Estevez", "2001/05/01", "CC", "EPS 1", "Sufre de algo"),
        (22, "Pedro Alzate", "2010/05/11", "TI", "EPS 2", "Sufre de artritis"),
        (33, "Juan Perez", "1998/05/28", "CC", "EPS 1", "No sufre de nada"),
        (47, "Maria Becerra", "1966/11/01", "CC", "EPS 1", "Sufre de todo"),
    ]
    cursor.executemany(insertar_tabla_paciente_sql, valores)
    print(f"Se han insertado {cursor.rowcount} registros")
    cursor.close()
