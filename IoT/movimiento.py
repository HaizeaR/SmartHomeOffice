import time
from grovepi import *
import math


#Clase que representa el comportamiento del sensor 3-axis accelerometer
class Movimiento():
    
    # constructor: se indica el puerto al que se va a conectar el sensor    
    def __init__(self):
        pass
    
    # método encargado de leer los valores 
    def calcularAceleracion(self):
        
        accl = acc_xyz()# Get the value from the accelerometer
        return accl
    
    # mide que no se detecte movimiento en ninguno d elos tres ejes x-y-z
    def situacionParada(self, accl):
        
        movimiento = False
        if (accl[0] == 0 and accl[1] == 0 and accl[2] == 0):
            movimiento = True
        else:
            movimiento = False
        return movimiento
    
    # mide que no se detecte movimiento en el eje X
    def situacionX(self, accl):
        movimiento = False
        if (accl[0] == 0):
            movimiento = True
        else:
            movimiento = False
        return movimiento
    
    # mide que no se detecte movimiento en el eje Y
    def situacionY(self, accl):
        movimiento = False
        if (accl[1] == 0):
            movimiento = True
        else:
            movimiento = False
        return movimiento
    
    # mide que no se detecte movimiento en el eje Z
    def situacionZ(self, accl):
        movimiento = False
        if (accl[2] == 0):
            movimiento = True
        else:
            movimiento = False
            
        return movimiento
    

