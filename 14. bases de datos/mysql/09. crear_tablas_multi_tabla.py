from Conexion import Conexion

conexion = Conexion.obtener_conexion_mysql()
cursor = conexion.cursor()

crear_tabla_medico_sql = """
    CREATE TABLE IF NOT EXISTS medico (
        id_medico INT AUTO_INCREMENT PRIMARY KEY,
        nombre_medico VARCHAR(50) NOT NULL,
        especialidad VARCHAR(50) NOT NULL
    ) 
"""
crear_tabla_citas_sql = """
    CREATE TABLE IF NOT EXISTS citas (
        id_cita INT AUTO_INCREMENT PRIMARY KEY,
        medico_asociado INT NOT NULL,
        paciente_asociado INT NOT NULL,
        fecha_cita DATE,
        hora_cita DECIMAL(4, 2),
        FOREIGN KEY (medico_asociado) REFERENCES medico(id_medico)
    ) 
"""
cursor.execute(crear_tabla_citas_sql)
conexion.commit()

cursor.close()
conexion.close()
