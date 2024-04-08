import numpy as np
import time
import os
tablero1 = np.full((11,11),"___")# pruebas de disparo inteligente. Depuración del fallo
tablero2 = np.full((11,11),"___")
tablero3 = np.full((11,11),"___")
tablero4 = np.full((11,11),"___")
marco = ["_0_","_1_","_2_","_3_","_4_","_5_","_6_","_7_","_8_","_9_","_10"]
tablero1[0:,:1] = np.reshape(marco,(11,1))
tablero1[:1,:] = np.reshape(marco,(1,11))
tablero2[0:,:1] = np.reshape(marco,(11,1))
tablero2[:1,:] = np.reshape(marco,(1,11))
tablero3[0:,:1] = np.reshape(marco,(11,1))
tablero3[:1,:] = np.reshape(marco,(1,11))
tablero4[0:,:1] = np.reshape(marco,(11,1))
tablero4[:1,:] = np.reshape(marco,(1,11))
turno_j = 1 # el comienzo de los turnos también debería ser aleatorio. habría que inicilializar los valores en 0, y mediante función aleatoria, poner un 1 en el que correspoda
turno_m = 1
coord1 = 4
coord2 = 4

tablero1[coord1, coord2]= "_B_"
tablero1[coord1, coord2+1]= "_B_"
tablero1[coord1, coord2+2]= "_B_"
tablero1[coord1, coord2+3]= "_B_"
 

#while turno_j == 1 :#parte por definir para ligar el juego y sus pasos
acierto = 0
enter = input("Presiona enter para disparar")
    # coord1 = np.random.randint(1,11)
    # coord2 = np.random.randint(1,11)
if enter == "":
    if "_B_" in tablero1[coord1, coord2]:
        tablero1[coord1, coord2] = "_X_"
        disparo1 = tablero1[coord1, coord2]
        tablero2[coord1, coord2] = "_X_"
        acierto+=1
        print("Has acertado!")
        print("\r{}".format(tablero1), end = "")
        print("\r{}".format(tablero2), end = "")
        enter1 = input("Presiona enter para volver a disparar")
        if enter1 == "":
            time.sleep(1)
            clear_screen()
            while acierto ==1:
                if "_B_" in tablero1[coord1-1:coord1+2, coord2-1:coord2+2]:
                    tablero1[coord1, coord2+1] = "_X_"
                    disparo1 = tablero1[coord1, coord2]
                    tablero2[coord1, coord2+1] = "_X_"
                    acierto+=1
                    print("Estas en racha!")
                    print("\r{}".format(tablero1), end = "")
                    print("\r{}".format(tablero2), end = "")
                    enter2 = input("Presiona enter para volver a disparar")
                    if enter2 == "":
                        time.sleep(1)
                        clear_screen()
                        while acierto ==2:
                            if "_B_" in tablero1[coord1-2:coord1+3, coord2-2:coord2+3]:
                                tablero1[coord1, coord2+2] = "_X_"
                                disparo1 = tablero1[coord1, coord2]
                                tablero2[coord1, coord2+2] = "_X_"
                                acierto+=1
                                print("Eres un fiera!")
                                #print(tablero1)
                                #print(tablero2)
                                while acierto ==3:
                                    if "_B_" in tablero1[coord1-3:coord1+4, coord2-3:coord2+4]:
                                        tablero1[coord1, coord2+3] = "_X_"
                                        disparo1 = tablero1[coord1, coord2]
                                        tablero2[coord1, coord2+3] = "_X_"
                                        acierto+=1
                                        #print(tablero1)
                                        #print(tablero2)
            #                         else:
            #                             print("has fallado")
            #                             acierto = 0
            #                             turno_j -= 1
            #                             turno_m += 1
            #                 else:
            #                     pass
            #         else:
            #             pass

    else: 
        print("fallo")


        turno_j -= 1
        #tablero1[coord1, coord2] = "_A_"
        #tablero2[coord1, coord2] = "_A_"
        #turno_j -= 1


        
        #turno_m += 1



#print(tablero1)

#print(tablero2)