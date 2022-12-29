from Conexion import Conexion

with Conexion.obtener_conexion_sqlite() as conexion:
    cursor = conexion.cursor()
    sentencia_sql = "SELECT * FROM paciente"
    cursor.execute(sentencia_sql)
    registros_encontrados = cursor.fetchall()

    for paciente in registros_encontrados:
        print(paciente)

    cursor.close()
