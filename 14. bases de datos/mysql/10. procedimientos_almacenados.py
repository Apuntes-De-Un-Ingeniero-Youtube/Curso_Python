from Conexion import Conexion

conexion = Conexion.obtener_conexion_mysql()
cursor = conexion.cursor()

crear_procedimiento_almacenado = """
    CREATE PROCEDURE insertar_medico (nombre_medico VARCHAR(50), especialidad VARCHAR(50))
    INSERT INTO medico (nombre_medico, especialidad) VALUES (nombre_medico, especialidad);
"""

ejecutar_procedimiento = "CALL insertar_medico(%s,%s)"
valores = ("Juanita", "Ortopedista")

cursor.execute(ejecutar_procedimiento, valores)
conexion.commit()
cursor.close()
conexion.close()
