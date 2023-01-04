import mysql.connector
import psycopg2
import sqlite3


class ConexionGenerica:

    __MYSQL_HOST = "localhost"
    __MYSQL_USER = "root"
    __MYSQL_PASSWORD = ""
    __MYSQL_DATABASE = "prueba_mysql"

    __POSTGRESQL_HOST = "127.0.0.1"
    __POSTGRESQL_PASSWORD = "admin"
    __POSTGRESQL_USER = "postgres"
    __POSTGRESQL_PORT = "5432"
    __POSTGRESQL_DATABASE = "prueba_postgres"

    __SQLITE_DATABASE = "./14. bases de datos/sqlite/prueba_sqlite.db"

    @classmethod
    def obtener_conexion_sqlite(self):
        return sqlite3.connect(self.__SQLITE_DATABASE)

    @classmethod
    def obtener_conexion_postgres(self):
        return psycopg2.connect(
            user=self.__POSTGRESQL_USER,
            password=self.__POSTGRESQL_PASSWORD,
            host=self.__POSTGRESQL_HOST,
            port=self.__POSTGRESQL_PORT,
            database=self.__POSTGRESQL_DATABASE
        )

    @classmethod
    def obtener_conexion_mysql(self):
        return mysql.connector.connect(
            host=self.__MYSQL_HOST,
            user=self.__MYSQL_USER,
            password=self.__MYSQL_PASSWORD,
            db=self.__MYSQL_DATABASE)


mysql = ConexionGenerica.obtener_conexion_mysql()
postgres = ConexionGenerica.obtener_conexion_postgres()
sqlite = ConexionGenerica.obtener_conexion_sqlite()

print(mysql)
print(postgres)
print(sqlite)
