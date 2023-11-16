from Servicio import Servicio

class Tv_Cable(Servicio):
    def __init__(self, cantidad_canales, nombre, precio_mensual, tipo):
        super().__init__(nombre, precio_mensual, tipo)
        self._cantidad_canales = cantidad_canales

    # Métodos de acceso para cantidad_canales
    def obtener_cantidad_canales(self):
        return self._cantidad_canales

    def establecer_cantidad_canales(self, nueva_cantidad):
        self._cantidad_canales = nueva_cantidad
