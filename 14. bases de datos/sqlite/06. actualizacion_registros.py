from Conexion import Conexion

with Conexion.obtener_conexion_sqlite() as conexion:
    cursor = conexion.cursor()
    sentencia_sql = """
        UPDATE paciente SET nombre = ?, fecha_nacimiento = ?  WHERE id_paciente = ?
    """
    # Actualizar un solo registro
    # valores = ("Juan Estevez 3", "2002/05/01", 111)
    # cursor.execute(sentencia_sql, valores)

    # Actualizar varios registros
    valores = [("Juan Estevez 3", "2002/05/01", 111),
               ("Pedro Alzate 3", "2010/07/11", 22),
               ("Maria Becerra 3", "1966/01/01", 47)]

    cursor.executemany(sentencia_sql, valores)
