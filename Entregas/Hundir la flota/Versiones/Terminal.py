"""Importación de librerias"""
import numpy
import time
import os
from IPython.display import clear_output
"""Importación de librerias"""

"""Definición del tablero"""
tablero1 = numpy.full((12,11),"___")
tablero2 = numpy.full((11,11),"___")
tablero3 = numpy.full((12,11),"___")
tablero4 = numpy.full((11,11),"___")

marco = ["=V=","_1_","_2_","_3_","_4_","_5_","_6_","_7_","_8_","_9_","_10"]
jugador1 = ["___","___","_J_","_U_","_G_","_A_","_D_","_O_","_R_","___","___"]
jugador2 = ["___","___","_M_","_A_","_Q_","_U_","_I_","_N_","_A_","___","___"]# buscar la opción de indicar el nº de vidas o barcos restantes en el título de la cuadrícula

tablero1[1:,:1] = numpy.reshape(marco,(11,1))
tablero1[1:2,:] = numpy.reshape(marco,(1,11))
tablero1[:1,:] = numpy.reshape(jugador1,(1,11))

tablero2[0:,:1] = numpy.reshape(marco,(11,1))
tablero2[:1,:] = numpy.reshape(marco,(1,11))

tablero3[1:,:1] = numpy.reshape(marco,(11,1))
tablero3[1:2,:] = numpy.reshape(marco,(1,11))
tablero3[:1,:] = numpy.reshape(jugador2,(1,11))

tablero4[0:,:1] = numpy.reshape(marco,(11,1))
tablero4[:1,:] = numpy.reshape(marco,(1,11))
"""Definición del tablero"""

""" Definición de variables"""
turno_j = 0 
turno_m = 1
flota_j = [1,1,1,1,2,2,2,3,3,4]
flota_m = [1,1,1,1,2,2,2,3,3,4]
n_barcos_j = len(flota_j)
portaaviones_j = flota_j.count(4)
acorazado_j = flota_j.count(3)
buque_j = flota_j.count(2)
fragata_j = flota_j.count(1)
n_barcos_m = len(flota_m)
portaaviones_m = flota_m.count(4)
acorazado_m = flota_m.count(3)
buque_m = flota_m.count(2)
fragata_m = flota_m.count(1)
n_portaaviones_j = 0
n_acorazado_j = 0
n_buque_j = 0
n_fragata_j = 0
n_barcos_j_ok = n_portaaviones_j +n_acorazado_j + n_buque_j +n_fragata_j
n_portaaviones_m = 0
n_acorazado_m = 0
n_buque_m = 0
n_fragata_m = 0
n_barcos_m_ok = n_portaaviones_m +n_acorazado_m + n_buque_m +n_fragata_m
n_vidas_j = sum(flota_j)
n_vidas_m = sum(flota_m)
a = 0
b = 0
# turno = int()
ganador_j = 0
ganador_m = 0
n_vidas_jugador = 20
n_vidas_maquina = 20



"""Definición de variables"""

#alternativa de orden para jugar

jugar = 1 #input("¿Quieres Jugar (S/N)?")
if jugar == 1:
#if jugar.lower() == "s":
    print("Genial! Pongamos nuestros barcos")
# if np.random.randint(0,2,1):
#     clear_output(wait=True)
#     time.sleep(1)
#     print("Que suerte, eres el primero en empezar")
#     #print(tablero1)
#     #print(tablero2)
#     #turno_j = 1
#     #time.sleep(2)       
#     #if turno_j == 1:    
    while n_portaaviones_j < portaaviones_j:
        if numpy.random.randint(0,2,1):
            orientacion = "horizontal"
            coord1 = numpy.random.randint(2,11)
            coord2 = numpy.random.randint(2,11-4+1)
        
            if "_B_" in tablero1[coord1-1:coord1+2, coord2-1:coord2+5]:
                #tablero1[coord1, coord2:coord2+size] = "C"
                pass
            else: 
                tablero1[coord1, coord2:coord2+4] = "_B_"
                n_portaaviones_j += 1
                #print(elemento)
        else:
            orientacion = "vertical"

            coord1 = numpy.random.randint(2,11-4+1)
            coord2 = numpy.random.randint(2,11)
        
            if "_B_" in tablero1[coord1-1:coord1+5, coord2-1:coord2+2]:
                #tablero1[coord1, coord2:coord2+size] = "C"
                pass
            else: 
                tablero1[coord1:coord1+4, coord2] = "_B_"
                n_portaaviones_j += 1
                    #print(elemento)
    while n_acorazado_j < acorazado_j:
        if numpy.random.randint(0,2,1):
            orientacion = "horizontal"
            coord1 = numpy.random.randint(2,11)
            coord2 = numpy.random.randint(2,11-3+1)
        
            if "_B_" in tablero1[coord1-1:coord1+2, coord2-1:coord2+4]:
                #tablero1[coord1, coord2:coord2+size] = "C"
                pass
            else: 
                tablero1[coord1, coord2:coord2+3] = "_B_"
                n_acorazado_j += 1
                #print(elemento)
        else:
            orientacion = "vertical"

            coord1 = numpy.random.randint(2,11-3+1)
            coord2 = numpy.random.randint(2,11)
        
            if "_B_" in tablero1[coord1-1:coord1+4, coord2-1:coord2+2]:
                #tablero1[coord1, coord2:coord2+size] = "C"
                pass
            else: 
                tablero1[coord1:coord1+3, coord2] = "_B_"
                n_acorazado_j += 1
                    #print(elemento)
    while n_buque_j < buque_j:
        if numpy.random.randint(0,2,1):
            orientacion = "horizontal"
            coord1 = numpy.random.randint(2,11)
            coord2 = numpy.random.randint(2,11-2+1)
        
            if "_B_" in tablero1[coord1-1:coord1+2, coord2-1:coord2+3]:
                #tablero1[coord1, coord2:coord2+size] = "C"
                pass
            else: 
                tablero1[coord1, coord2:coord2+2] = "_B_"
                n_buque_j += 1
                #print(elemento)
        else:
            orientacion = "vertical"

            coord1 = numpy.random.randint(2,11-2+1)
            coord2 = numpy.random.randint(2,11)
        
            if "_B_" in tablero1[coord1-1:coord1+3, coord2-1:coord2+2]:
                #tablero1[coord1, coord2:coord2+size] = "C"
                pass
            else: 
                tablero1[coord1:coord1+2, coord2] = "_B_"
                n_buque_j += 1
                    #print(elemento)
    while n_fragata_j < fragata_j:
        if numpy.random.randint(0,2,1):
            orientacion = "horizontal"
            coord1 = numpy.random.randint(2,11)
            coord2 = numpy.random.randint(2,11)
        
            if "_B_" in tablero1[coord1-1:coord1+2, coord2-1:coord2+2]:
                #tablero1[coord1, coord2:coord2+size] = "C"
                pass
            else: 
                tablero1[coord1, coord2:coord2+1] = "_B_"
                n_fragata_j += 1
                #print(elemento)
        else:
            orientacion = "vertical"

            coord1 = numpy.random.randint(2,11)
            coord2 = numpy.random.randint(2,11)
        
            if "_B_" in tablero1[coord1-1:coord1+2, coord2-1:coord2+2]:
                #tablero1[coord1, coord2:coord2+size] = "C"
                pass
            else: 
                tablero1[coord1:coord1+1, coord2] = "_B_"
                n_fragata_j += 1
                    #print(elemento)  
# print(tablero1)
# print(tablero2)
#     clear_output(wait=True)
#     time.sleep(1)
#     print(tablero1)
#     print(tablero2)
#     # clear_output(wait=True)
#     # time.sleep(1)
#     # print("tamos ready")
# else:
#     clear_output(wait=True)
#     time.sleep(1)
#     print("Oh vaya, te toca esperar")
#     # print(tablero3)
#     # print(tablero4)
#     #turno_m = 1 
#     #time.sleep(2)
#     #if turno_m == 1:
    while n_portaaviones_m < portaaviones_m:
        if np.random.randint(0,2,1):
            orientacion = "horizontal"
            coord3 = numpy.random.randint(2,11)
            coord4 = numpy.random.randint(2,11-4+1)
        
            if "_B_" in tablero3[coord3-1:coord3+2, coord4-1:coord4+5]:
                #tablero1[coord3, coord4:coord4+size] = "C"
                pass
            else: 
                tablero3[coord3, coord4:coord4+4] = "_B_"
                n_portaaviones_m += 1
                #print(elemento)
        else:
            orientacion = "vertical"

            coord3 = numpy.random.randint(2,11-4+1)
            coord4 = numpy.random.randint(2,11)
        
            if "_B_" in tablero3[coord3-1:coord3+5, coord4-1:coord4+2]:
                #tablero1[coord3, coord4:coord4+size] = "C"
                pass
            else: 
                tablero3[coord3:coord3+4, coord4] = "_B_"
                n_portaaviones_m += 1
                    #print(elemento)
    while n_acorazado_m < acorazado_m:
        if numpy.random.randint(0,2,1):
            orientacion = "horizontal"
            coord3 = numpy.random.randint(2,11)
            coord4 = numpy.random.randint(2,11-3+1)
        
            if "_B_" in tablero3[coord3-1:coord3+2, coord4-1:coord4+4]:
                #tablero1[coord3, coord4:coord4+size] = "C"
                pass
            else: 
                tablero3[coord3, coord4:coord4+3] = "_B_"
                n_acorazado_m += 1
                #print(elemento)
        else:
            orientacion = "vertical"

            coord3 = numpy.random.randint(2,11-3+1)
            coord4 = numpy.random.randint(2,11)
        
            if "_B_" in tablero3[coord3-1:coord3+4, coord4-1:coord4+2]:
                #tablero1[coord3, coord4:coord4+size] = "C"
                pass
            else: 
                tablero3[coord3:coord3+3, coord4] = "_B_"
                n_acorazado_m += 1
                    #print(elemento)
    while n_buque_m < buque_m:
        if numpy.random.randint(0,2,1):
            orientacion = "horizontal"
            coord3 = numpy.random.randint(2,11)
            coord4 = numpy.random.randint(2,11-2+1)
        
            if "_B_" in tablero3[coord3-1:coord3+2, coord4-1:coord4+3]:
                #tablero1[coord3, coord4:coord4+size] = "C"
                pass
            else: 
                tablero3[coord3, coord4:coord4+2] = "_B_"
                n_buque_m += 1
                #print(elemento)
        else:
            orientacion = "vertical"

            coord3 = numpy.random.randint(2,11-2+1)
            coord4 = numpy.random.randint(2,11)
        
            if "_B_" in tablero3[coord3-1:coord3+3, coord4-1:coord4+2]:
                #tablero1[coord3, coord4:coord4+size] = "C"
                pass
            else: 
                tablero3[coord3:coord3+2, coord4] = "_B_"
                n_buque_m += 1
                    #print(elemento)
    while n_fragata_m < fragata_m:
        if numpy.random.randint(0,2,1):
            orientacion = "horizontal"
            coord3 = numpy.random.randint(2,11)
            coord4 = numpy.random.randint(2,11)
        
            if "_B_" in tablero3[coord3-1:coord3+2, coord4-1:coord4+2]:
                #tablero1[coord3, coord4:coord4+size] = "C"
                pass
            else: 
                tablero3[coord3, coord4:coord4+1] = "_B_"
                n_fragata_m += 1
                #print(elemento)
        else:
            orientacion = "vertical"

            coord3 = numpy.random.randint(2,11)
            coord4 = numpy.random.randint(2,11)
        
            if "_B_" in tablero3[coord3-1:coord3+2, coord4-1:coord4+2]:
                #tablero1[coord3, coord4:coord4+size] = "C"
                pass
            else: 
                tablero3[coord3:coord3+1, coord4] = "_B_"
                n_fragata_m += 1
                    #print(elemento)  

    clear_output(wait=True)
    time.sleep(3)# nos da 3 segundos de Genial! Pongamos nuestros barcos
    print(tablero1)
    print(tablero3)

    clear_output(wait=True)
    time.sleep(3)
    print("Veamos quien empieza")

    if np.random.randint(0,2,1):
        clear_output(wait=True)
        time.sleep(2)
        print("Que suerte, eres el primero en empezar, empieza disparando!")
        a = 1
        turno = 1
        
        
    else:
        clear_output(wait=True)
        time.sleep(2)
        print("Te toca esperar, empiezo disparando!")
        b = 1
        turno = 0
while (ganador_m == 0) and (ganador_j == 0):
    enter = input("Presiona enter para continuar")  
    if enter == "":
        if a == 1:
            coord1 = numpy.random.randint(2,12)
            coord2 = numpy.random.randint(1,11)
            if "_B_" in tablero1[coord1, coord2]:
                tablero1[coord1, coord2] = "_X_"
                #disparo1 = tablero1[coord1, coord2]
                tablero2[coord1-1, coord2] = "_X_"
                clear_output(wait=True)
                print("Me has dado!")
                print(tablero1)
                print(tablero2)  
                a = 1
                b = 0
                n_vidas_maquina-=1
                # if turno == 1:
                #     turno = 1
            elif "_A_" in tablero1[coord1, coord2]:
                pass
                
            else:
                tablero1[coord1, coord2] = "_A_"
                tablero2[coord1-1, coord2] = "_A_"
                acierto = 0
                clear_output(wait=True)
                #time.sleep(1)
                print("Has fallado, ahora me toca a mi")
                print(tablero1)
                print(tablero2)  
                a = 0
                b = 1
                # if turno == 1:
                #     turno = 0
        elif b == 1:
            coord1 = numpy.random.randint(2,12)
            coord2 = numpy.random.randint(1,11)
            if "_B_" in tablero1[coord1, coord2]:
                tablero3[coord1, coord2] = "_X_"
                #disparo1 = tablero3[coord1, coord2]
                tablero4[coord1-1, coord2] = "_X_"
                clear_output(wait=True)
                print("Te he dado!")
                print(tablero3)
                print(tablero4)  
                b = 1
                a = 0
                n_vidas_jugador-=1
                # if turno == 0:
                #     turno = 0
            elif "_A_" in tablero1[coord1, coord2]:
                pass
            else:
                tablero3[coord1, coord2] = "_A_"
                tablero4[coord1-1, coord2] = "_A_"
                acierto = 0
                clear_output(wait=True)
                #time.sleep(1)
                print("He fallado, ahora te toca a ti")
                print(tablero3)
                print(tablero4)  
                b = 0
                a = 1
                # if turno == 0:
                #     turno = 1
if n_vidas_jugador == 0:
    gandor_m = 1
elif n_vidas_maquina == 0:
    gandor_j = 1