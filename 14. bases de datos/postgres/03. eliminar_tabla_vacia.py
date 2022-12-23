import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='prueba_postgres'
)

cursor = conexion.cursor()

eliminar_tabla_citas_sql = "DROP TABLE IF EXISTS mi_tabla_2;"

cursor.execute(eliminar_tabla_citas_sql)

conexion.commit()

cursor.close()
conexion.close()
