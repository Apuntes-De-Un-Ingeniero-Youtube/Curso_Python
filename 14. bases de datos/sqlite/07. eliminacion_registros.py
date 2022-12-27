from Conexion import Conexion

with Conexion.obtener_conexion_sqlite() as conexion:
    cursor = conexion.cursor()
    setencia_sql = "DELETE FROM paciente WHERE id_paciente = ?"
    dato_eliminar = tuple(input("Ingrese el id del paciente a eliminar: "))
    cursor.execute(setencia_sql, dato_eliminar)
    cursor.close()

    """ Para eliminar varios registros hacemos los siguiente """
    setencia_sql = "DELETE FROM paciente WHERE id_paciente IN ?"
    dato_eliminar = input(
        "Ingrese el id de los pacientes a eliminar (separados por coma): ")
    valores = list(tuple(dato_eliminar.split(",")),)
    cursor.execute(setencia_sql, dato_eliminar, valores)
    cursor.close()
