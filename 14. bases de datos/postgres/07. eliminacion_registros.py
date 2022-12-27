from Conexion import Conexion

with Conexion.obtener_conexion_postgres() as conexion:
    with conexion.cursor() as cursor:
        sentencia_sql = "DELETE FROM citas WHERE id_cita IN %s"

        # Elimina un solo registro
        # eliminacion = tuple(input("Ingrese el id de la cita a eliminar "))
        # cursor.execute(sentencia_sql, eliminacion)

        # Elimina varios registros
        entrada = input("Ingresa el id de las citas a eliminar (separadas por coma) ")
        eliminacion = (tuple(entrada.split(",")),)
        cursor.execute(sentencia_sql, eliminacion)
        print(f"{cursor.rowcount} registros eliminados")
