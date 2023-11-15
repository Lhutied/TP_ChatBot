from Usuario import Usuario

class Cliente(Usuario):
    def __init__(self, nombre, apellido, correo, edad, ciudad, codCliente):
        super().__init__(nombre,apellido,correo,edad,ciudad)
        self._codCliente = codCliente



