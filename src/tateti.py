# -*- coding: utf-8 -*-
'''
Created on 30/05/2013

@author: YANI
'''
# Tateti por consola ISP20
# License: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
#
# Website - http://www.isp20.edu.ar
import sys
import os
#creo un diccionario con los sistemas operativos como clave y los comandos
#que borran las consola como valores
comandos = {"posix":"clear","nt":"cls"}
 
#hago un diccionario con cada una de las posiciones posibles como clave y como valor
#un espacio en blanco que ubicar� la marca de cada jugador cuando la elijan
#para colocar su ficha
 
posiciones_tablero={1:" ",2:" ",3:" ",4:" ",5:" ",6:" ",7:" ",8:" ",9:" "}
 
#elaboramos un dicionario con las fichas de los 2 jugadores, cada ficha tendr� un posici�n
#asociada, inician en cero los valores, a medida que vayan definiendo posiciones
#se ir�n almacenando en el correspondiente diccionario y clave-ficha
fichas_jugadores = {1:{1:0,2:0,3:0},2:{1:0,2:0,3:0}}
marcas_jugadores = {1:"X",2:"O"}
#determino quien comienza a jugar y que ficha va a mover
jugador_actual = 1
ficha_actual = 1
 
def PintarTablero():
    '''utilizo el diccionario con comandos y pasandole la clave que
       retorna os.name que nos dice el sistema operativo en el que estamos'''
    #borro la consola
    os.system(comandos[os.name])
    for nro in range(1,10):
        #imprime los corchetes uno al lado del otro
        sys.stdout.write("[%s]"%posiciones_tablero[nro])
        if (nro%3==0): print "\n"
    ##lineas para debug, para poder hacer un seguimiento de la evoluci�n
    ##de los diccionarios
    #print "posiciones_tablero"
    #print posiciones_tablero
    #print "fichas_jugadores"
    #print fichas_jugadores
 
def Jugar(jugador_actual=0, ficha_actual=0):
    pos_jugada = input("Jugador %i: ingrese posicion para la ficha %i:" % (jugador_actual, ficha_actual))
    fichas_jugadores[jugador_actual][ficha_actual]=pos_jugada
    posiciones_tablero[pos_jugada]=marcas_jugadores[jugador_actual]
         
 
while True:
    PintarTablero()
    if (ficha_actual==0):
        ficha_actual=input("Jugador %i ingrese el número de ficha a mover:" % jugador_actual)
    '''    
    Jugar(jugador_actual, ficha_actual)
    jugador_actual+=1
    if jugador_actual == 3 :
        jugador_actual = 1
        ficha_actual+=1
        if ficha_actual == 4:
            ficha_actual = 0
            '''
    posicion_elegida=input("Jugador %i: Ingrese la posicion de la ficha %i: " % (jugador_actual,ficha_actual))
    posiciones_tablero[posicion_elegida]=marcas_jugadores[jugador_actual]
    jugador_actual+=1
    if jugador_actual == 3:
        jugador_actual = 1
        ficha_actual+=1
        if ficha_actual == 4:
            ficha_actual = 0