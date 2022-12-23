import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    db="prueba_mysql")

# Crear un cursosr para ejecutar consultas
cursor = conexion.cursor()

# Definir el SQL para insertar datos en la tabla
# insertar_tabla_paciente_sql = """
#     INSERT INTO medico (
#         nombre,
#         tipo_identificacion,
#         numero_tarjeta_profesional,
#         anios_experiencia,
#         especialidad,
#         hora_inicio_atencion,
#         hora_fin_atencion
#     ) VALUES (%s,%s,%s,%s,%s,%s,%s);
# """
# valores = ("Juan Médico", "CC", "#F78", 5.7, "Urología", 8.30, 16.25)

# Definir el SQL para insertar datos en la tabla
# insertar_tabla_paciente_sql = """
#     INSERT INTO medico (
#         nombre,
#         especialidad,
#         hora_fin_atencion
#     ) VALUES (%s,%s,%s);
# """
# valores = ("Juan Médico 2", "Neurología", 18)

# Definir el SQL para insertar todos datos en la tabla
insertar_tabla_paciente_sql = """
    INSERT INTO medico VALUES (%s,%s,%s,%s,%s,%s,%s,%s);
"""
valores = (77, "Juan Médico", "CC", "#F7I8", 5.7, "Urología", 8.30, 16.25)

# Ejecutar consulta
cursor.execute(insertar_tabla_paciente_sql, valores)

# Haciendo el commit
conexion.commit()

# Cerrando objetos
cursor.close()
conexion.close()
