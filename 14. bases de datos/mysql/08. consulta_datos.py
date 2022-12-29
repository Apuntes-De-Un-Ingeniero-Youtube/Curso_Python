from Conexion import Conexion

conexion = Conexion.obtener_conexion_mysql()
cursor = conexion.cursor()

sentencia_sql = "SELECT * FROM medico"
cursor.execute(sentencia_sql)
registros_encontrados = cursor.fetchall()

for medico in registros_encontrados:
    print(medico)

conexion.commit()
cursor.close()
conexion.close()
