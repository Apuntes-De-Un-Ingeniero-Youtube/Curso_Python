import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='prueba_postgres'
)

cursor = conexion.cursor()

insertar_tabla_citas_sql = """
    INSERT INTO citas (medico_asociado, paciente_asociado, fecha_cita, hora_cita) 
    VALUES (%s,%s,%s,%s)
"""

valores = (1, 2, "2021/01/07", 12)

cursor.execute(insertar_tabla_citas_sql, valores)

conexion.commit()

cursor.close()
conexion.close()
