from Conexion import Conexion

with Conexion.obtener_conexion_postgres() as conexion:
    with conexion.cursor() as cursor:
        sentencia_sql = """
        CREATE OR REPLACE FUNCTION insertar_medico(id INT, nombre VARCHAR(50), especialidad VARCHAR(50)) 
        RETURNS void AS $$
        BEGIN
            INSERT INTO medico (id_medico, nombre_medico, especialidad) VALUES (id, nombre, especialidad);
        END;
        $$ LANGUAGE plpgsql;
        """
        # cursor.execute(sentencia_sql)
        ejecutar_funcion = "SELECT insertar_medico(%s, %s, %s)"
        valores = (12, "Leonardo", "Cardiología")
        cursor.execute(ejecutar_funcion, valores)

