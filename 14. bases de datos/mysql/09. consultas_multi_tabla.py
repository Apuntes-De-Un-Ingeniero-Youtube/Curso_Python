from Conexion import Conexion

conexion = Conexion.obtener_conexion_mysql()
cursor = conexion.cursor()

sentencia_sql = "SELECT * FROM citas INNER JOIN medico ON citas.medico_asociado = medico.id_medico WHERE id_medico = 1"
cursor.execute(sentencia_sql)
registro = cursor.fetchone()
print(registro)
