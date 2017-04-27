#!/usr/bin/python
# -*- coding: utf-8 -*-

from socket import socket
import funciones_cliente2
from easygui import passwordbox
def main():
    server= socket()
    server.connect(('127.0.0.1', 9090))
    x=True
    y=1
    z=True

    while True:
        #enviar mensaje del cliente
        if z== True:
            print "ingrese correo y presione enter"
        if x== True:
            mensaje_cliente = raw_input("Ingrese Mensaje al Servidor >> ")
            if y==1:
                x=False
        else:
            mensaje_cliente = passwordbox("Ingrese Mensaje al Servidor >> ")
            x=True
            y=2



        if mensaje_cliente:
            try:
                server.send(mensaje_cliente)
            except TypeError:
                server.send(bytes(mensaje_cliente, "utf-8"))

        #respuesta servidor

        #mensaje_servidor = server.recv(1024)
        #if mensaje_servidor:
         #   print mensaje_servidor

        mensaje_servidor = server.recv(1024)
        funciones_cliente2.imprimir(mensaje_servidor)


if __name__ == '__main__':
    main()






