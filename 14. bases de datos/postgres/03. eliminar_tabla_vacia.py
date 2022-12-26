from Conexion import Conexion

with Conexion.obtener_conexion_postgres() as conexion:
    with conexion.cursor() as cursor:
        eliminar_tabla_citas_sql = "DROP TABLE IF EXISTS mi_tabla_2;"
        cursor.execute(eliminar_tabla_citas_sql)
