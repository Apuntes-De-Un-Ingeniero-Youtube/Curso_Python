import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    db="prueba_mysql")

# Crear un cursosr para ejecutar consultas
cursor = conexion.cursor()

# Definir el SQL para crear la tabla
crear_tabla_paciente_sql = """
    CREATE TABLE medico (
        id_medico INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(50) NOT NULL,
        tipo_identificacion VARCHAR(10) NOT NULL,
        numero_tarjeta_profesional VARCHAR(20) UNIQUE,
        anios_experiencia DECIMAL(3,1) NOT NULL,
        especialidad VARCHAR(50) NOT NULL,
        hora_inicio_atencion DECIMAL(4, 2) NOT NULL,
        hora_fin_atencion DECIMAL(4, 2) NOT NULL
    );
"""

# Ejecutar consulta
cursor.execute(crear_tabla_paciente_sql)

# Haciendo el commit
conexion.commit()

# Cerrando objetos
cursor.close()
conexion.close()
