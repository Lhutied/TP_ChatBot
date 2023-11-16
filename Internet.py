from Servicio import Servicio

class Internet(Servicio):
    def __init__(self, velocidad, nombre, precio_mensual, tipo):
        super().__init__(nombre, precio_mensual, tipo)
        self._velocidad = velocidad

    # Métodos de acceso para velocidad
    def obtener_velocidad(self):
        return self._velocidad

    def establecer_velocidad(self, nueva_velocidad):
        self._velocidad = nueva_velocidad