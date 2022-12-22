import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='prueba_postgres'
)

cursor = conexion.cursor()

crear_tabla_citas_sql = """
    CREATE TABLE citas (
        id_cita SERIAL PRIMARY KEY,
        medico_asociado INTEGER NOT NULL,
        paciente_asociado INTEGER NOT NULL,
        fecha_cita DATE,
        hora_cita DECIMAL(4, 2)
    )
"""

cursor.execute(crear_tabla_citas_sql)

conexion.commit()

cursor.close()
conexion.close()
