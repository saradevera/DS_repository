import numpy as np
from time import sleep
from clase import *
tablero = Tablero()
tablero.inicia_tablero()


# FUNCION CREACION BARCOS

def barco_aleatorio_maquina(eslora):
    '''
    La función barco_aleatorio genera de manera aleatoria las coordenadas de posición de un barco de eslora determinada.
    Inputs: eslora - > int
    Output: coordenadas barco -> list
    '''
    coordenadas_barco = []
    fila = np.random.randint(0,10)
    columna = np.random.randint(0,10)
    orien = np.random.choice(["N", "S", "E", "O"])
    
    while len(coordenadas_barco) < eslora:
        if orien == "N":
            fila = fila - 1
            if fila-eslora<-3:
                return barco_aleatorio_maquina(eslora)
                
        if orien == "S":
            fila = fila + 1
            if fila+eslora>12:
                return barco_aleatorio_maquina(eslora)
        
        if orien == "E":
            columna = columna + 1
            if columna+eslora>12:
                return barco_aleatorio_maquina(eslora)
        
        if orien == "O":
            columna = columna - 1
            if columna-eslora<-3:
                return barco_aleatorio_maquina(eslora)
        
        coordenadas_barco.append((fila, columna))

    return coordenadas_barco


def barco_por_coordenadas_jugador(eslora):
    '''
    La función barco_aleatorio genera de manera aleatoria las coordenadas de posición de un barco de eslora determinada.
    Inputs: eslora - > int
    Output: coordenadas barco -> list
    '''
    coordenadas_barco = []
    fila = int(input('Escribe aquí la primera coordenada'))
    columna = int(input('Escribe aquí la segunda coordenada'))
    orien = input('Escribe aquí la orientación, a elegir: "N", "S", "E", "O"').upper()

    while len(coordenadas_barco) < eslora:
        if orien == "N":
            fila = fila - 1
            if fila-eslora<-4:
                return barco_aleatorio_maquina(eslora)
                
        if orien == "S":
            fila = fila + 1
            if fila+eslora>13:
                return barco_aleatorio_maquina(eslora)
        
        if orien == "E":
            columna = columna + 1
            if columna+eslora>13:
                return barco_aleatorio_maquina(eslora)
        
        if orien == "O":
            columna = columna - 1
            if columna-eslora<-4:
                return barco_aleatorio_maquina(eslora)
      
        coordenadas_barco.append((fila, columna))

    return coordenadas_barco



def colocar_barco_jugador(tablero, barco_por_coordenadas_jugador):
    '''
    La función colocar_barco posiciona dentro del tablero el barco de coordenadas generadas por la función barco_aleatorio
    Input: variable tablero
    Input: lista de coordenadas
    Output: tablero modificado
    '''

    for elem in barco_por_coordenadas_jugador:
        tablero[elem] = "\U0001F680"
        print("Colocando barco en posicion", elem)
        sleep(0.5)
        
    return tablero

def colocar_barcos_jugador(tablero, barcos):

    for barco in barcos:
        tablero = colocar_barco_jugador(tablero, barco)
    return tablero


def colocar_barco_maquina(tablero, barco_aleatorio_maquina):
    '''
    La función colocar_barco posiciona dentro del tablero el barco de coordenadas generadas por la función barco_aleatorio
    Input: variable tablero
    Input: lista de coordenadas
    Output: tablero modificado
    '''
    for elem in barco_aleatorio_maquina:
        tablero[elem] = '\U0001F680'
    return tablero

def colocar_barcos_maquina(tablero,barcos):

    for barco in barcos:
        tablero = colocar_barco_maquina(tablero, barco)
    print("La máquina ha colocado todos sus barcos")
    


# FUNCIONES DISPARO

def disparo_por_coordenadas_DOBLE_TAB(tablero, tablero_2):
    '''
    La función disparo por coordenadas, modifica el tablero en las coordenadas que se han aportado como argumento. 
    Input: variable tablero
    Output : tablero modificado
    '''
    coordenada1=int(input('Escribe aquí la primera coordenada'))
    coordenada2=int(input('Escribe aquí la segunda coordenada'))
    '\U000026AA' == False

    while True: 
        if tablero[coordenada1,coordenada2] == '\U000026AA':
            
            tablero[coordenada1,coordenada2] = '\U0001F537'
            tablero_2[coordenada1,coordenada2] = '\U0001F537'
            
            print("Agua, has perdido el turno...")
            print(tablero_2)
            
            break


        elif tablero[coordenada1,coordenada2] == '\U0001F680':
            
            tablero[coordenada1,coordenada2] = '\U00002B55'
            tablero_2[coordenada1,coordenada2] = '\U00002B55'

            print("Tocado, ¡sigue disparando!")
            print(tablero_2)

            coordenada1=int(input('Escribe aquí la primera coordenada'))
            coordenada2=int(input('Escribe aquí la segunda coordenada'))

    
            
def disparo_aleatorio_con_bucle(tablero):
    '''
    La función disparo, modifica el tablero en las coordenadas que se han aportado como argumento. 
    Input: variable tablero
    Input: coordenadas
    Output : tablero modificado
    '''
    
    coordenada1=np.random.randint(0,10)
    coordenada2=np.random.randint(0,10)
    '\U000026AA' == False
       

    while True:
        if tablero[coordenada1,coordenada2] == '\U000026AA':
            print('Máquina disparando...')
            sleep(1)

            tablero[coordenada1,coordenada2] = '\U0001F537'
            print("La máquina ha fallado")
            break
               
        elif tablero[coordenada1,coordenada2] == '\U0001F680':
            print('Máquina disparando...')
            sleep(1)
            
            tablero[coordenada1,coordenada2] = '\U00002B55'
            print("La máquina ha impactado una de tus naves")
            print(tablero)

            return disparo_aleatorio_con_bucle
        
    return tablero