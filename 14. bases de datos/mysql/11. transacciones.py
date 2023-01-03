from Conexion import Conexion

conexion = Conexion.obtener_conexion_mysql()
cursor = conexion.cursor()

# Definir el SQL para insertar todos datos en la tabla
insertar_tabla_paciente_sql = """
    INSERT INTO medico VALUES (%s,%s,%s,%s,%s,%s,%s,%s);
"""
valores = (77000, "Juan Médico borrar", "CC", "#F7jhggoI8",
           5.7, "Urología", 8.30, 16.25)
try:
    # Ejecutar consulta
    cursor.execute(insertar_tabla_paciente_sql, valores)
    conexion.commit()
except Exception as e:
    print("Ha ocurrido un error " + e)
    conexion.rollback()
finally:
    cursor.close()
    conexion.close()
