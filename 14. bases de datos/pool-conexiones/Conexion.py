from psycopg2 import pool
import sys


class Conexion:

    __HOST = "127.0.0.1"
    __PASSWORD = "admin"
    __USER = "postgres"
    __PORT = "5432"
    __DATABASE = "prueba_postgres"
    __MIN_CON = 1
    __MAX_CON = 5
    _pool = None

    @classmethod
    def obtener_pool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls.__MIN_CON, cls.__MAX_CON, host=cls.__HOST,
                                                      user=cls.__USER, password=cls.__PASSWORD,
                                                      port=cls.__PORT, database=cls.__DATABASE)
                return cls._pool
            except Exception as e:
                print(e)
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtener_conexion(cls):
        conexion = cls.obtener_pool().getconn()
        return conexion

    @classmethod
    def liberar_conexion(cls, conexion):
        cls.obtener_pool().putconn(conexion)

    @classmethod
    def cerrar_conexiones(cls):
        cls.obtener_pool().closeall()
