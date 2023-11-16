import sqlite3
from Cliente import Cliente
from Factura import Factura

class DAL(object):
    def __init__(self):
        self.conn = sqlite3.connect('simulacion.db')
        self.cursor = self.conn.cursor()


########################################################### USUARIOS ###########################################################

    @staticmethod
    def crear_usuarios(): 
        return [
            Cliente(nombre="John", apellido="Doe", correo="john@example.com", edad=25, ciudad="New York", codCliente=111222),
            Cliente(nombre="Jane", apellido="Doe", correo="jane@example.com", edad=30, ciudad="Los Angeles", codCliente=111333),
            Cliente(nombre="Alice", apellido="Smith", correo="alice@example.com", edad=22, ciudad="Chicago", codCliente=111444),
            Cliente(nombre="Eva", apellido="Johnson", correo="eva@example.com", edad=28, ciudad="Miami", codCliente=111555),
            Cliente(nombre="David", apellido="Brown", correo="david@example.com", edad=35, ciudad="Houston", codCliente=111666),
            Cliente(nombre="Sophia", apellido="Miller", correo="sophia@example.com", edad=26, ciudad="San Francisco", codCliente=111777),
            Cliente(nombre="Daniel", apellido="Wilson", correo="daniel@example.com", edad=31, ciudad="Seattle", codCliente=111888),
            Cliente(nombre="Olivia", apellido="Moore", correo="olivia@example.com", edad=24, ciudad="Denver", codCliente=111999),
            Cliente(nombre="Matthew", apellido="Taylor", correo="matthew@example.com", edad=29, ciudad="Dallas", codCliente=111000)
        ]

    def inicializar_base_datos(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                apellido TEXT,
                correo TEXT,
                edad INTEGER,
                ciudad TEXT,
                codCliente INTEGER
            )
        ''')

        usuarios = self.crear_usuarios()
        for usuario in usuarios:
            self.cursor.execute('INSERT INTO usuarios VALUES (NULL, ?, ?, ?, ?, ?, ?)', 
                                (usuario._nombre, usuario._apellido, usuario._correo, usuario._edad, usuario._ciudad, usuario._codCliente))
        self.conn.commit()

    def obtener_usuarios_desde_db(self):
        self.cursor.execute('SELECT * FROM usuarios')
        usuarios_en_db = self.cursor.fetchall()

        usuarios = []
        for usuario in usuarios_en_db:
            usuarios.append(Cliente(nombre=usuario[1], apellido=usuario[2], correo=usuario[3], edad=usuario[4], ciudad=usuario[5], codCliente=usuario[6]))

        return usuarios

########################################################### FACTURAS ###########################################################


    def crear_tabla_facturas(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS facturas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                numero TEXT,
                fecha TEXT,
                cliente_id INTEGER,
                total REAL,
                FOREIGN KEY (cliente_id) REFERENCES usuarios(id)
            )
        ''')
        self.conn.commit()

    def insertar_factura(self, factura):
        self.cursor.execute('INSERT INTO facturas VALUES (NULL, ?, ?, ?, ?)',
                            (factura.obtener_numero(), factura.obtener_fecha(),
                             factura.obtener_cliente().obtener_cod_cliente(), factura.obtener_total()))
        self.conn.commit()

    def obtener_facturas_cliente(self, cliente):
        self.cursor.execute('SELECT * FROM facturas WHERE cliente_id = ?', (cliente.obtener_cod_cliente(),))
        facturas_en_db = self.cursor.fetchall()

        facturas = []
        for factura_en_db in facturas_en_db:
            factura = Factura(numero=factura_en_db[1], fecha=factura_en_db[2], total=factura_en_db[4])
            facturas.append(factura)

        return facturas

dal = DAL()
dal.inicializar_base_datos()
dal.crear_tabla_facturas()


## Facturas de ejemplo ##

clientes = dal.obtener_usuarios_desde_db()

for cliente in clientes: 
    for i in range(5):
        factura = Factura(numero=f"FA{i+1}", fecha="2023-01-01", cliente=cliente, total=100.0)
        dal.insertar_factura(factura)


########################################################### TV ## INTERNET ## PRODUCTOS ###########################################################
