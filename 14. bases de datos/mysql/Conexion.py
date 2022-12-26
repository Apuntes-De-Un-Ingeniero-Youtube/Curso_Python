import mysql.connector


class Conexion:

    __HOST = "localhost"
    __USER = "root"
    __PASSWORD = ""
    __DATABASE = "prueba_mysql"

    @classmethod
    def obtener_conexion_mysql(self):
        return mysql.connector.connect(
            host=self.__HOST,
            user=self.__USER,
            password=self.__PASSWORD,
            db=self.__DATABASE)

