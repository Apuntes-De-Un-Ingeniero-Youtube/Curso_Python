from Conexion import Conexion

with Conexion.obtener_conexion_sqlite() as conexion:
    cursor = conexion.cursor()

    sentencia_sql = "SELECT * FROM citas INNER JOIN paciente ON citas.paciente_asociado = paciente.id_paciente WHERE id_paciente = 1"
    cursor.execute(sentencia_sql)
    registro = cursor.fetchone()
    print(registro)
