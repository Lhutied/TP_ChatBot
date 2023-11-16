from Usuario import Usuario

class Cliente(Usuario):
    def __init__(self, nombre, apellido, correo, edad, ciudad, codCliente):
        super().__init__(nombre, apellido, correo, edad, ciudad)
        self._codCliente = codCliente
        self._facturas = []

    def obtener_cod_cliente(self):
        return self._codCliente

    def establecer_cod_cliente(self, nuevo_cod_cliente):
        self._codCliente = nuevo_cod_cliente

    def obtener_facturas(self):
        return self._facturas

    def agregar_factura(self, factura):
        self._facturas.append(factura)

    def agregar_tv_cable(self, tv_cable):
        self._facturas[-1].agregar_producto(tv_cable)

    def agregar_internet(self, internet):
        self._facturas[-1].agregar_producto(internet)

    def agregar_producto(self, producto):
        self._facturas[-1].agregar_producto(producto)