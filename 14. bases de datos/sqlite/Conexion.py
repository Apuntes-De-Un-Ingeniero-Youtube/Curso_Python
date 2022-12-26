import sqlite3


class Conexion:

    __DATABASE = "./14. bases de datos/sqlite/prueba_sqlite.db"

    @classmethod
    def obtener_conexion_sqlite(self):
        return sqlite3.connect(self.__DATABASE)
