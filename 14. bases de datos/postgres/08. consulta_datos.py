from Conexion import Conexion

with Conexion.obtener_conexion_postgres() as conexion:
    with conexion.cursor() as cursor:
        sentencia_sql = "SELECT * FROM citas WHERE id_cita IN %s"
        datos = input("Ingresa las citas a consultar separadas por coma ")
        datos_a_buscar = (tuple(datos.split(",")),)
        cursor.execute(sentencia_sql, datos_a_buscar)
        registros_encontrados = cursor.fetchall()
        # print(registros_encontrados)
        for cita in registros_encontrados:
            print(cita)
