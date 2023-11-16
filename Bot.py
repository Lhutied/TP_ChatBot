# -*- coding: utf-8 -*-

##definicion de atributos
class Bot:
    def __init__(self, nombre="", version=1.0, desarrollador="", activo=False):
        self._nombre = nombre
        self._version = version
        self._desarrollador = desarrollador
        self._activo = activo

    # metodos de acceso - encapsulamiento
    def obtener_nombre(self):
        return self._nombre

    def establecer_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def obtener_version(self):
        return self._version

    def establecer_version(self, nueva_version):
        self._version = nueva_version

    def obtener_desarrollador(self):
        return self._desarrollador

    def establecer_desarrollador(self, nuevo_desarrollador):
        self._desarrollador = nuevo_desarrollador

    def esta_activo(self):
        return self._activo

    def activar(self):
        self._activo = True

    def desactivar(self):
        self._activo = False

    def ejecutar_accion(self, accion):
        print(f"Bot ejecuta la accion: {accion}")
        
########## Definicion de funcionamiento de opciones de usuario
    def __init__(self):
            self.opciones = {
                1: self.opcion_internet,
                2: self.opcion_telefonia,
                3: self.opcion_tv_cable,
                4: self.opcion_consultas_administrativas,
                5: self.opcion_baja_servicio,
                6: self.opcion_comunicarse_con_agente,
                11: self.opcion_servicio_contratado,
                12: self.opcion_problemas_conexion,
                13: self.opcion_gestionar_modem
            }

    def opcion_internet(self): ##opcion 1
        print("Seleccionaste Internet \n")
        print("11. Consultar Servicio Contratado")
        print("12. Problemas de Conexion")
        print("13. Gestionar Modem")
        
    def opcion_servicio_contratado(self): ## opcion 11
        print("Seleccionaste Servicio Contratado \n")
        

    def opcion_problemas_conexion(self): ##opcion 12
        print("Seleccionaste problemas de Conexion \n")
    
    def opcion_gestionar_modem(self): ##opcion 13
        print("Seleccionaste Gestionar Modem \n")

    def opcion_telefonia(self): ##opcion 2
        print("Seleccionaste Telefonia")

    def opcion_tv_cable(self): ##opcion 3
        print("Seleccionaste TV Cable")

    def opcion_consultas_administrativas(self): ##opcion 4
        print("Seleccionaste Consultas Administrativas")

    def opcion_baja_servicio(self): ##opcion 5
        print("Seleccionaste Baja de Servicio")

    def opcion_comunicarse_con_agente(self): ##opcion 6
        print("Seleccionaste Comunicarse con un Agente")
    
    def menu_principal(self):
        print("\nSelecciona la opcion deseada\n")
        print("1. Internet")
        print("2. Telefonia")
        print("3. TV Cable")
        print("4. Consultas Administrativas")
        print("5. Baja de Servicio")
        print("6. Comunicarse con un Agente")
        
# Crear una instancia de la clase Bot
mi_bot = Bot()

# Diccionario que asocia opciones con métodos de la instancia de la clase Bot
# opciones = {
#     1: mi_bot.opcion_internet,
#     2: mi_bot.opcion_telefonia,
#     3: mi_bot.opcion_tv_cable,
#     4: mi_bot.opcion_consultas_administrativas,
#     5: mi_bot.opcion_baja_servicio,
#     6: mi_bot.opcion_comunicarse_con_agente
# }

    