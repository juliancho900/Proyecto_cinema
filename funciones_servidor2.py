#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import json
import time
import os
import MySQLdb
import datetime

DB_HOST = '127.0.0.1'
DB_USER = 'root'
DB_PASS = ''
DB_NAME = 'cinema'



def run_query(query=''):
    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]

    conn = MySQLdb.connect(*datos)  # Conectar a la base de datos
    cursor = conn.cursor()  # Crear un cursor
    cursor.execute(query)  # Ejecutar una consulta

    if query.upper().startswith('SELECT'):
        data = cursor.fetchall()  # Traer los resultados de un select
    else:
        conn.commit()  # Hacer efectiva la escritura de datos
        data = None

    cursor.close()  # Cerrar el cursor
    conn.close()  # Cerrar la conexión

    return data

#Funciones Administrador

def ver_pelicula():
    query = "SELECT nom_pelicula FROM pelicula "
    result = run_query(query)
    cadena = json.dumps(result)
    return cadena

def pedir_pelicula():
    lista = ["Ingrese pelicula y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def pedir_valor_taquilla():
    lista = ["Ingrese valor de la entrada y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def pedir_sillas_sala():
    lista = ["Ingrese cantidad de sillas dela sala y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def nueva_pelicula():
    lista = ["Ingrese La Nueva Pelicula y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def agregar_pelicula(dato,dato2,dato3):
    query = "INSERT INTO pelicula (nom_pelicula,valor_taquilla,sillas_disponibles) VALUES ('%s','%s','%s')" % (dato,dato2,dato3)
    run_query(query)
    lista = ["pelicula Creada Satisfactoriamente, Presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def actualizar_pelicula(b1,b2):

    query = "UPDATE pelicula SET b2='%s' WHERE b1 = %i" % (b2, int(b1))
    run_query(query)

def ver_factura():
    query = "SELECT nombre_pelicula,valor_taquilla,horario_venta,fecha_venta FROM facturacion"
    result = run_query(query)
    cadena = json.dumps(result)
    return cadena
def detalle_factura():
    query = "SELECT *FROM facturacion"
    result = run_query(query)
    cadena = json.dumps(result)
    return cadena


#Menus Usuario Cliente
def menu_pelicula():
    lista = ["Cinema Lola", "1. comprar pase", "2. Puntos",
             "3. Facturas", "4. Salir", "Digite la opcion >>"]
    cadena = json.dumps(lista)
    return cadena

def menu_comprar_pase():
    lista = ["compra pase", "1. Ver lista peliculas", "2. Seleccionar Pelicula",
             "3. Generar Facturaa", "4. Pagar pase",
             "5. Salir", "Digite la opcion >>"]
    cadena = json.dumps(lista)
    return cadena

def menu_puntos():
    lista = ["Puntos", "1. Ver Puntos", "2. Cambiar Puntos ",
             "3. Salir", "Digite la opcion >>"]
    cadena = json.dumps(lista)
    return cadena
def menu_facturas():
    lista = ["facturas", "1. Ver facturas", "2. detalles facturas ",
             "3. Salir", "Digite la opcion >>"]
    cadena = json.dumps(lista)
    return cadena
#Menus Usuario Administrador

def menu_1():
    lista = ["Cinema Lola (Administrador)", "1. Alertas", "2. Peliculas",
             "3. Ventas", "4. Usuarios", "5. Log Usuarios",
             "6. Salir", "Digite la opcion >>"]
    cadena = json.dumps(lista)
    return cadena

def menu_alertas():
    lista = ["Alertas", "1. Maximo sillas alcanzadas", "2. Salir", "Digite la opcion >>"]
    cadena = json.dumps(lista)
    return cadena

def menu_peliculas():
    lista = ["peliculas", "1. Listado Peliculas", "2. Agregar Pelicula",
             "3. Actualizar Peliculas", "4. Salir", "Digite la opcion >>"]
    cadena = json.dumps(lista)
    return cadena

def menu_ventas():
    lista = ["Ventas", "1. Listado facturas", "2. Detalle Factura",
             "3. Ventas Totales Dia", "4. Salir", "Digite la opcion >>"]
    cadena = json.dumps(lista)
    return cadena

def menu_usuario():
    lista = ["Usuario", "1. Listado Usuario", "2. Usuarios y Puntos",
             "3. Crear Usuario", "4. Salir", "Digite la opcion >>"]
    cadena = json.dumps(lista)
    return cadena

def menu_log_usuario():
    lista = ["Log Usuario", "1. Reportes", "2. Salir", "Digite la opcion >>"]
    cadena = json.dumps(lista)
    return cadena





#Funciones Usuario Cliente
def usuarios():
    lista = ["Ingrese usuario y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def validar_usuario(cadena,ip):
    x = [[cadena]]
    query = "SELECT correo FROM usuario WHERE correo = '%s'" % cadena
    result = run_query(query)
    user = json.dumps(x)
    y = json.dumps(result)
    if(y == user):
        creartxt()
        archivo = open('datos.txt', 'a')
        fecha = time.strftime("%x")
        hora = time.strftime("%X")
        archivo.write("Usuario " + cadena + '\n')
        archivo.write("Ip " + str(ip) + '\n')
        archivo.write("Fecha " + fecha + '\n')
        archivo.write("Hora " + hora + '\n')
        archivo.close()
        return True

    else:
        creartxt()
        archivo = open('datos.txt', 'a')
        fecha = time.strftime("%x")
        hora = time.strftime("%X")
        archivo.write("Usuario " + cadena + '\n')
        archivo.write("Ip " + str(ip) + '\n')
        archivo.write("Fecha " + fecha + '\n')
        archivo.write("Hora " + hora + '\n')
        archivo.close()
        return True
def validar_contrasena(comprador,cadena):
    x = [[comprador,cadena]]
    query = "SELECT correo,contrasena FROM usuario WHERE correo = '%s' and contrasena = '%s' " % (comprador,cadena)
    result = run_query(query)
    user = json.dumps(x)
    y = json.dumps(result)
    if (y == user):



        return True
    else:
        return False


def horario_pelicula():
    lista= ["Ingrese horario de la pelicula y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena
def cupos_pelicula():
    lista = ["Ingrese cantidad de boletas  y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena
def dinero_taquilla(r):
    valor = r*10000
    lista = ["el valor a pagar es: $"+ str(valor)]
    cadena = json.dumps(lista)
    return cadena
def pago_taquilla():
    lista = ["Ingrese la denominacion del dinero y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena
def confirmar_pago():
    lista = ["confirmar pago de las boletas (S/N) y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena
def generar_pago(a,r):
    b= 10000*r
    resultado = a-b
    lista = ["dinero recibido $"+str(a)+ '\n'+
             "valor taquilla $" + str(b) + '\n' +
             "devuelta cliente $" + str(resultado)]
    cadena = json.dumps(lista)
    return cadena
def generar_factura(nombre,persona,cupo,a,r):
    fecha = time.strftime("%x")
    hora = time.strftime("%X")

    valor = 10000*r

    query = "INSERT INTO facturacion(nombre_pelicula,nombre_cliente,cupos_pelicula,horario_venta,fecha_venta,valor_taquilla) VALUES ('%s','%s','%s','%s','%s','%s')"%(nombre,persona,cupo,hora,fecha,valor)
    run_query(query)

    puntos= valor/100
    query = "INSERT INTO puntos(nombre_cliente,puntos_cliente) VALUES ('%s','%s')"%(persona,puntos)
    run_query(query)
    b = 10000 * r
    resultado = a - b
    lista = ["dinero recibido $" + str(a) + '\n' +
             "valor taquilla $" + str(b) + '\n' +
             "devuelta cliente $" + str(resultado)+ '\n' +
             "facturacion realizada, presione enter "]
    cadena = json.dumps(lista)
    return cadena


def ver_puntos(cliente):
    query = "SELECT nombre_cliente, puntos_cliente FROM puntos WHERE nombre_cliente = '%s'" % cliente
    result = run_query(query)
    #print result
    cadena = json.dumps(result)
    return cadena
def pedir_producto():
    lista= ["Ingrese producto que desea cajear por sus puntos y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena
def cambiar_puntos(comprador,producto):
    query = "SELECT puntos_cliente FROM puntos WHERE nombre_cliente = '%s'" % comprador
    result = run_query(query)
    cadena = json.dumps(result)

    query = "SELECT puntos_producto FROM productos WHERE nombre_producto = '%s'" % producto
    result = run_query(query)
    # print result
    b = json.dumps(result)
    if cadena == b:
        lista = ["sus puntos fueron canjeados exitosamente y presione enter >>"]
    else:
        lista = ["no tiene suficientes puntos, siga comprando y presione enter >>"]
    n = json.dumps(lista)
    return n


def ver_productos():
    query = "SELECT nombre_producto,puntos_producto FROM productos "
    result = run_query(query)
    cadena = json.dumps(result)
    return cadena

def ver_facturas(comprador):
    query = "SELECT nombre_pelicula,valor_taquilla FROM facturacion WHERE nombre_cliente = '%s'" % comprador
    result = run_query(query)
    cadena = json.dumps(result)
    return cadena
def detalle_facturas(comprador):
    query = "SELECT *FROM facturacion WHERE nombre_cliente = '%s'" % comprador
    result = run_query(query)
    cadena = json.dumps(result)
    return cadena
def comprobar_cupo_pelicula(cupo,pelicula):
    query = "SELECT sillas_disponibles FROM pelicula WHERE nom_pelicula = '%s'" % pelicula
    result = run_query(query)
    cadena = json.dumps(result)
    print cadena
    if cupo > cadena:
        return True
    else:
        return False
def mensaje():
    lista = ["no hay sillas dsiponibles para esta pelicula y presione enter >>"]
    n = json.dumps(lista)
    return n

def fecha_diario():
    lista = ["Ingrese la fecha (dd/mm/aaaa) y presione enter >>"]
    k = json.dumps(lista)
    return k

def total_ventas(fecha):
    query = "SELECT nombre_pelicula,valor_taquilla FROM facturacion  WHERE fecha_venta = '%s'" % fecha
    result = run_query(query)
    cadena = json.dumps(result)
    return cadena

def lista_usuario():
    query = "SELECT * FROM usuario"
    result = run_query(query)
    cadena = json.dumps(result)
    return cadena

def usuario_puntos():
    query = "SELECT * FROM puntos"
    result = run_query(query)
    cadena = json.dumps(result)
    return cadena

def contrasena():
    lista = ["Ingrese su contrasena y presione enter >>"]
    k = json.dumps(lista)
    return k
def pedir_usuario():
    lista = ["Ingrese su nombre y presione enter >>"]
    k = json.dumps(lista)
    return k
def pedir_cedula():
    lista = ["Ingrese su cedula y presione enter >>"]
    k = json.dumps(lista)
    return k
def tipo_usuario():
    lista = ["Ingrese tipo de usuario y presione enter >>"]
    k = json.dumps(lista)
    return k
def correo_usuario():
    lista = ["Ingrese su correo y presione enter >>"]
    k = json.dumps(lista)
    return k
def contra_usuario():
    lista = ["Ingrese su contrasena y presione enter >>"]
    h = json.dumps(lista)
    return h
def crea_usuario(user,cedula,tipo,correo, contra):
    fecha = datetime.date.today()
    z= fecha.strftime("%d/%m/%y")
    query = "INSERT INTO usuario (id_cedula,nombre_usuario,tipo_usuario,correo,contrasena,fecha_registro) VALUES ('%s','%s','%s','%s','%s','%s')" % (cedula,user,tipo,correo,contra,z)
    run_query(query)
    lista = ["Usuario Creado Exitosamente y presione enter >>"]
    h = json.dumps(lista)
    return h
def creartxt():
    archivo=open('datos.txt','w')
    archivo.close()

def reportes():
    archivo = str('datos.txt')
    archi = open(archivo, 'r')
    lineas=archi.readlines()
    texto=str(lineas)
    lista = ["Contenido del Archivo "+ archivo + '\n' + texto]
    cadena = json.dumps(lista)
    archi.close()
    return cadena






