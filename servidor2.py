#!/usr/bin/python
# -*- coding: utf-8 -*-

from socket import socket, error
from threading import Thread
import funciones_servidor2
import json


class Cliente(Thread):

    '''funcion que genera hilos'''
    def __init__(self, con, dire):
        Thread.__init__(self)
        self.conexion = con
        self.direccion= dire


    def run(self):
        while True:
            try:
                a=False
                b=False
                while (a!= True):
                    while (b!=True):
                        mensaje_cliente=self.conexion.recv(1024)
                        comprador=mensaje_cliente

                        mensaje_cliente = funciones_servidor2.validar_usuario(mensaje_cliente,ip)
                        usuario=mensaje_cliente
                        if usuario == True:
                            mensaje_cliente = funciones_servidor2.contrasena()
                            self.conexion.send(mensaje_cliente)
                            mensaje_cliente = int(self.conexion.recv(1024))
                            operacion = mensaje_cliente
                            mensaje_cliente = funciones_servidor2.validar_contrasena(comprador,operacion)
                            contrasena = mensaje_cliente
                            b = True
                        else:
                            mensaje_cliente = funciones_servidor2.pedir_usuario()
                            self.conexion.send(mensaje_cliente)
                            mensaje_cliente = str(self.conexion.recv(1024))
                            comprador = mensaje_cliente
                            b = True
                            contrasena = False



                    while (contrasena == True):
                        menu = False
                        while (menu != True):
                            mensaje_cliente=funciones_servidor2.menu_1()
                            self.conexion.send(mensaje_cliente)
                            mensaje_cliente = int(self.conexion.recv(1024))
                            operacion=mensaje_cliente
                            if operacion ==1 :
                                mensaje_cliente = funciones_servidor2.menu_alertas()
                                self.conexion.send(mensaje_cliente)
                                #num_1 = str(self.conexion.recv(1024))
                                #mensaje_cliente = funciones_servidor2.getnum_2()
                                #self.conexion.send(mensaje_cliente)

                            if operacion ==2:
                                mensaje_cliente = funciones_servidor2.menu_peliculas()
                                self.conexion.send(mensaje_cliente)
                                mensaje_cliente = int(self.conexion.recv(1024))
                                dato = mensaje_cliente
                                if  dato == 1:
                                    mensaje_cliente = funciones_servidor2.ver_pelicula()
                                    self.conexion.send(mensaje_cliente)
                                    #mensaje_cliente = int(self.conexion.recv(1024))
                                if  dato == 2:
                                    mensaje_cliente = funciones_servidor2.pedir_pelicula()
                                    self.conexion.send(mensaje_cliente)
                                    mensaje_cliente = str(self.conexion.recv(1024))
                                    dato = mensaje_cliente
                                    mensaje_cliente = funciones_servidor2.pedir_valor_taquilla()
                                    self.conexion.send(mensaje_cliente)
                                    mensaje_cliente = int(self.conexion.recv(1024))
                                    dato2 = mensaje_cliente
                                    mensaje_cliente = funciones_servidor2.pedir_sillas_sala()
                                    self.conexion.send(mensaje_cliente)
                                    mensaje_cliente = int(self.conexion.recv(1024))
                                    dato3 = mensaje_cliente
                                    mensaje_cliente = funciones_servidor2.agregar_pelicula(dato,dato2,dato3)
                                    self.conexion.send(mensaje_cliente)
                                if dato == 3:
                                    #mensaje_cliente = funciones_servidor2.ver_pelicula()
                                    #self.conexion.send(mensaje_cliente)
                                    mensaje_cliente = funciones_servidor2.pedir_pelicula()
                                    self.conexion.send(mensaje_cliente)
                                    mensaje_cliente = (self.conexion.recv(1024))
                                    num1 = mensaje_cliente
                                    mensaje_cliente = funciones_servidor2.nueva_pelicula()
                                    self.conexion.send(mensaje_cliente)
                                    mensaje_cliente = (self.conexion.recv(1024))
                                    num2 = mensaje_cliente
                                    mensaje_cliente = funciones_servidor2.actualizar_pelicula(num1,num2)
                                    self.conexion.send(mensaje_cliente)





                            if operacion == 3:
                                mensaje_cliente = funciones_servidor2.menu_ventas()
                                self.conexion.send(mensaje_cliente)
                                mensaje_cliente = int(self.conexion.recv(1024))
                                dato = mensaje_cliente
                                if dato == 1:
                                    mensaje_cliente = funciones_servidor2.ver_factura()
                                    self.conexion.send(mensaje_cliente)
                                if dato == 2:
                                    mensaje_cliente = funciones_servidor2.detalle_factura()
                                    self.conexion.send(mensaje_cliente)
                                if dato == 3:
                                    mensaje_cliente = funciones_servidor2.fecha_diario()
                                    self.conexion.send(mensaje_cliente)
                                    mensaje_cliente = str(self.conexion.recv(1024))
                                    fecha = mensaje_cliente
                                    mensaje_cliente = funciones_servidor2.total_ventas(fecha)
                                    self.conexion.send(mensaje_cliente)




                            if operacion == 4:
                                mensaje_cliente = funciones_servidor2.menu_usuario()
                                self.conexion.send(mensaje_cliente)
                                mensaje_cliente = int(self.conexion.recv(1024))
                                dato = mensaje_cliente
                                if dato == 1:
                                    mensaje_cliente = funciones_servidor2.lista_usuario()
                                    self.conexion.send(mensaje_cliente)
                                if dato == 2:
                                    mensaje_cliente = funciones_servidor2.usuario_puntos()
                                    self.conexion.send(mensaje_cliente)
                                if dato == 3:
                                    mensaje_cliente = funciones_servidor2.pedir_usuario()
                                    self.conexion.send(mensaje_cliente)
                                    mensaje_cliente = str(self.conexion.recv(1024))
                                    user = mensaje_cliente
                                    mensaje_cliente = funciones_servidor2.pedir_cedula()
                                    self.conexion.send(mensaje_cliente)
                                    mensaje_cliente = int(self.conexion.recv(1024))
                                    cedula = mensaje_cliente
                                    mensaje_cliente = funciones_servidor2.tipo_usuario()
                                    self.conexion.send(mensaje_cliente)
                                    mensaje_cliente = str(self.conexion.recv(1024))
                                    tipo = mensaje_cliente
                                    mensaje_cliente = funciones_servidor2.correo_usuario()
                                    self.conexion.send(mensaje_cliente)
                                    mensaje_cliente = str(self.conexion.recv(1024))
                                    correo = mensaje_cliente
                                    mensaje_cliente = funciones_servidor2.contra_usuario()
                                    self.conexion.send(mensaje_cliente)
                                    mensaje_cliente = str(self.conexion.recv(1024))
                                    contra = mensaje_cliente
                                    mensaje_cliente = funciones_servidor2.crea_usuario(user,cedula,tipo,correo, contra)
                                    self.conexion.send(mensaje_cliente)


                            if operacion == 5:
                                mensaje_cliente = funciones_servidor2.menu_log_usuario()
                                self.conexion.send(mensaje_cliente)
                                mensaje_cliente = int(self.conexion.recv(1024))
                                dato = mensaje_cliente
                                if dato == 1:
                                    mensaje_cliente = funciones_servidor2.reportes()
                                    self.conexion.send(mensaje_cliente)


                            if operacion == 6:
                                pass

                            if operacion == 7:
                                pass

                    menu_1=False
                    while (menu_1!= True):
                        mensaje_cliente = funciones_servidor2.menu_pelicula()
                        self.conexion.send(mensaje_cliente)
                        mensaje_cliente = int(self.conexion.recv(1024))
                        operacion = mensaje_cliente

                        if operacion == 1:
                            mensaje_cliente = funciones_servidor2.menu_comprar_pase()
                            self.conexion.send(mensaje_cliente)
                            mensaje_cliente = int(self.conexion.recv(1024))
                            dato = mensaje_cliente
                            if dato == 1:
                                mensaje_cliente = funciones_servidor2.ver_pelicula()
                                self.conexion.send(mensaje_cliente)
                                # mensaje_cliente = int(self.conexion.recv(1024))
                            if dato == 2:
                                mensaje_cliente = funciones_servidor2.ver_pelicula()
                                self.conexion.send(mensaje_cliente)

                                mensaje_cliente = funciones_servidor2.pedir_pelicula()
                                self.conexion.send(mensaje_cliente)
                                mensaje_cliente = str(self.conexion.recv(1024))
                                y = mensaje_cliente
                                mensaje_cliente = funciones_servidor2.horario_pelicula()
                                self.conexion.send(mensaje_cliente)
                                mensaje_cliente = str(self.conexion.recv(1024))
                                t = mensaje_cliente
                                mensaje_cliente = funciones_servidor2.cupos_pelicula()
                                self.conexion.send(mensaje_cliente)
                                mensaje_cliente = int(self.conexion.recv(1024))
                                r = mensaje_cliente
                                mensaje_cliente = funciones_servidor2.comprobar_cupo_pelicula(r,y)
                                o = mensaje_cliente
                                if o == True:
                                    mensaje_cliente = funciones_servidor2.dinero_taquilla(r)
                                    self.conexion.send(mensaje_cliente)

                                    mensaje_cliente = funciones_servidor2.pago_taquilla()
                                    self.conexion.send(mensaje_cliente)
                                    mensaje_cliente = int(self.conexion.recv(1024))
                                    e = mensaje_cliente
                                    mensaje_cliente = funciones_servidor2.confirmar_pago()
                                    self.conexion.send(mensaje_cliente)
                                    mensaje_cliente = str(self.conexion.recv(1024))
                                    u = mensaje_cliente
                                    if u == "s":
                                        mensaje_cliente = funciones_servidor2.generar_factura(y,comprador,r,e,r)
                                        self.conexion.send(mensaje_cliente)
                                else:
                                    mensaje_cliente = funciones_servidor2.mensaje()
                                    self.conexion.send(mensaje_cliente)







                            #mensaje_cliente = funciones_servidor2.getnum_2()
                            #self.conexion.send(mensaje_cliente)

                        if operacion == 2:
                            mensaje_cliente = funciones_servidor2.menu_puntos()
                            self.conexion.send(mensaje_cliente)
                            mensaje_cliente = int(self.conexion.recv(1024))
                            c = mensaje_cliente

                            if c == 1:
                                mensaje_cliente = funciones_servidor2.ver_puntos(comprador)
                                self.conexion.send(mensaje_cliente)
                            if c == 2:
                                #mensaje_cliente = funciones_servidor2.ver_puntos(comprador)
                                #self.conexion.send(mensaje_cliente)

                                mensaje_cliente = funciones_servidor2.ver_productos()
                                self.conexion.send(mensaje_cliente)

                                mensaje_cliente = funciones_servidor2.pedir_producto()
                                self.conexion.send(mensaje_cliente)
                                mensaje_cliente = str(self.conexion.recv(1024))
                                v = mensaje_cliente
                                mensaje_cliente = funciones_servidor2.cambiar_puntos(comprador,v)
                                self.conexion.send(mensaje_cliente)

                        if operacion == 3:
                            mensaje_cliente = funciones_servidor2.menu_facturas()
                            self.conexion.send(mensaje_cliente)
                            mensaje_cliente = int(self.conexion.recv(1024))
                            c = mensaje_cliente

                            if c == 1:
                                mensaje_cliente = funciones_servidor2.ver_facturas(comprador)
                                self.conexion.send(mensaje_cliente)
                            if c == 2:
                                mensaje_cliente = funciones_servidor2.detalle_facturas(comprador)
                                self.conexion.send(mensaje_cliente)




                        if operacion == 4:
                            pass

                        if operacion == 5:
                            pass
                            #mensaje_cliente = funciones_servidor2.usuarios()
                            #self.conexion.send(mensaje_cliente)
                            #mensaje_cliente = self.conexion.recv(1024)
                            #menu_1 = True
                            #usuario=True
                            #menu= False
            except error:
                print("[%s] Error de lectura "%self.name)
                break
            else:
                if mensaje_cliente:
                    self.conexion.send(mensaje_cliente)



def main():
    server = socket()
    server.bind(("127.0.0.1", 9090))
    server.listen(1)


    while True:
        con, dire = server.accept()
        hilo= Cliente(con, dire)
        hilo.start()
        print("conexion de %s:%d " %dire)
        #hilo =Thread(target=funciones_servidor2.menu,args=())
        #hilo.start()

if __name__ == '__main__':
    main()

