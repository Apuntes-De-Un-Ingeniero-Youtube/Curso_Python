from Conexion import Conexion


class CursorDelPool:

    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        self._conexion = Conexion.obtener_conexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipo_exception, valor_excepcion, detalle_excepcion):
        if valor_excepcion:
            self._conexion.rollback()
        else:
            self._conexion.commit()
        self._cursor.close()
        Conexion.liberar_conexion(self._conexion)
