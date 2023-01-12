import psycopg2


class Conexion:

    __HOST = "127.0.0.1"
    __PASSWORD = "admin"
    __USER = "postgres"
    __PORT = "5432"
    __DATABASE = "prueba_postgres"

    @classmethod
    def obtener_conexion_postgres(self):
        return psycopg2.connect(
            user=self.__USER,
            password=self.__PASSWORD,
            host=self.__HOST,
            port=self.__PORT,
            database=self.__DATABASE
        )
