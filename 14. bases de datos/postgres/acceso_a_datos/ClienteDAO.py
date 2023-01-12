from Conexion import Conexion
from Cliente import Cliente


class ClienteDAO:

    _SELECCIONAR = 'SELECT * FROM cliente ORDER BY id_cliente'
    _INSERTAR = 'INSERT INTO cliente(nombre_cliente, apellido_cliente, email, razon_social, telefono) VALUES(%s, %s, %s, %s, %s)'
    _ACTUALIZAR = 'UPDATE cliente SET nombre_cliente=%s, apellido_cliente=%s, email=%s, telefono=%s WHERE razon_social=%s'
    _ELIMINAR = 'DELETE FROM cliente WHERE id_cliente=%s'
    _OBTNER_POR_RAZON_SOCIAL = "SELECT * FROM cliente WHERE razon_social=%s"

    @classmethod
    def seleccionar(cls):
        with Conexion.obtener_conexion_postgres() as conexion:
            with conexion.cursor() as cursor:
                clientes = []
                try:
                    cursor.execute(cls._SELECCIONAR)
                    registros = cursor.fetchall()
                    for registro in registros:
                        cliente = Cliente(
                            registro[5], registro[0], registro[1], registro[2], registro[3], registro[4])
                        clientes.append(cliente)
                    return clientes
                except Exception as e:
                    print(e)
                    return clientes

    @classmethod
    def insertar(cls, cliente):
        with Conexion.obtener_conexion_postgres() as conexion:
            with conexion.cursor() as cursor:
                try:
                    valores = (cliente.get_nombre(),
                               cliente.get_apellido(),
                               cliente.get_email(),
                               cliente.get_razon_social(),
                               cliente.get_telefono())
                    cursor.execute(cls._INSERTAR, valores)
                    return cursor.rowcount
                except Exception as e:
                    print(e)
                    return 0

    @classmethod
    def actualizar(cls, cliente, razon_social):
        with Conexion.obtener_conexion_postgres() as conexion:
            with conexion.cursor() as cursor:
                try:
                    valores = (cliente.get_nombre(),
                               cliente.get_apellido(),
                               cliente.get_email(),
                               cliente.get_telefono(),
                               razon_social)
                    cursor.execute(cls._ACTUALIZAR, valores)
                    return cursor.rowcount
                except Exception as e:
                    print(e)
                    return 0

    @classmethod
    def eliminar(cls, cliente):
        with Conexion.obtener_conexion_postgres() as conexion:
            with conexion.cursor() as cursor:
                try:
                    valores = (cliente.get_id_cliente(),)
                    cursor.execute(cls._ELIMINAR, valores)
                    return cursor.rowcount
                except Exception as e:
                    print(e)
                    return 0

    @classmethod
    def consultar_por_razon_social(cls, razon_social):
        with Conexion.obtener_conexion_postgres() as conexion:
            with conexion.cursor() as cursor:
                try:
                    valores = (razon_social,)
                    cursor.execute(cls._OBTNER_POR_RAZON_SOCIAL, valores)

                    if cursor.rowcount == 1:
                        registro = cursor.fetchone()

                        nombre = registro[0]
                        apellido = registro[1]
                        email = registro[2]
                        razon_social_obtenida = registro[3]
                        telefono = registro[4]
                        id_cliente = registro[5]

                        cliente = Cliente(id_cliente, nombre, apellido,
                                          email, razon_social_obtenida, telefono)
                        return cliente

                    return -1
                except Exception as e:
                    print(e)
                    return 0
