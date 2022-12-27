from Conexion import Conexion

conexion = Conexion.obtener_conexion_mysql()
cursor = conexion.cursor()

sentencia_sql = "DELETE FROM medico WHERE id_medico = %s"
eliminacion = tuple(input("Ingrese el id del médico a eliminar "))

cursor.execute(sentencia_sql, eliminacion)

conexion.commit()
cursor.close()
conexion.close()

"""
    Para eliminar varios registros se debe hacer exactamente lo mismo que con postgres
    se crea una tupla de tupla y se cambia la sentencia SQL por la siguiente:

    DELETE FROM medico WHERE id_medico IN %s
"""
