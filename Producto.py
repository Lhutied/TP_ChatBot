class Producto(object):
    def __init__(self, nombre="", descripcion="", precio=0.0):
        self._nombre = nombre
        self._descripcion = descripcion
        self._precio = precio

    def obtener_nombre(self):
        return self._nombre

    def establecer_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def obtener_descripcion(self):
        return self._descripcion

    def establecer_descripcion(self, nueva_descripcion):
        self._descripcion = nueva_descripcion

    def obtener_precio(self):
        return self._precio

    def establecer_precio(self, nuevo_precio):
        self._precio = nuevo_precio