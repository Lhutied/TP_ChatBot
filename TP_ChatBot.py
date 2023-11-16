#importar clases y directivas
import os
from os import access, system
# -*- coding: utf-8 -*-

from inspect import isclass
from multiprocessing.connection import Client
from operator import isub
from re import S
from warnings import catch_warnings
from Agente import Agente
from Cliente import Cliente
from Usuario import Usuario
from Bot import Bot
from DAL import DAL

## obtener usuarios desde DB

acceso = DAL()

Lista_usuarios = acceso.obtener_usuarios_desde_db()


## Otras instancias

botardo = Bot()

##

##Limpia Consola

def limpiar(): 
    os.system('cls')
    print('\n' * 50)



## Menu principal
print('\n' * 50)
print("Hola, Bienvenido al 'Compu Hiper Mega Red'. Ya sos cliente? \n")
print("Si") 
print("No \n")

isUser = input() 


if isUser == 'Si' or 'si':
    limpiar()

    isDocumento = int( input("Por favor ingrese su numero de documento : \n"))
    print(isDocumento)
    
    for isClient in Lista_usuarios:
        buscaDNI = isClient._codCliente
        if isDocumento == buscaDNI:
            actualClient = isClient
            break            
       
    if actualClient:
        limpiar()
        
        print(f"Hola: {actualClient._nombre}. En que lo puedo ayudar? \n")
         
        botardo.menu_principal() ## muestra opciones
        
        opcionUsuario = int(input())
        
        while True:
            try:
                if opcionUsuario in botardo.opciones:
                    limpiar()
                    botardo.opciones[opcionUsuario]()
                    opcionUsuario = int(input())
                
                    if opcionUsuario in botardo.opciones:
                        limpiar()
                        botardo.opciones[opcionUsuario]()
                        opcionUsuario = int(input())
                else:
                    limpiar()
                    print("Opcion invalida. Intente nuevamente.")
                    botardo.menu_principal()  ## muestra opciones
                    opcionUsuario = int(input())
            except ValueError :
                limpiar()
                print("Opcion invalida. Intente nuevamente.")
                                  
    else:
        limpiar()
        print("No se encontro un cliente asociado al numero de documento")

else:
    print("\n Selecciona la opcion deseada \n" )
    
    print("7. Contratar un Servicio")
    
