import time
from grovepi import *
import math

class Movimiento():
    
    def __init__(self):
        pass
    
    def calcularAcceleracion(self):
        
        accl = acc_xyz()# Get the value from the accelerometer
        return accl
    
    # mide que no se detecte movimiento en ninguno d elos tres ejes x-y-z
    def situacionParada(self, accl):
        
        if (accl[0] == 0 and accl[1] == 0 and accl[2] == 0):
            return True
        else:
            return False
        
    # mide que no se detecte movimiento en el eje X
    def situacionX(self, accl):
        
        if (accl[0] == 0):
            return True
        else:
            return False
        
    # mide que no se detecte movimiento en el eje Y
    def situacionY(self, accl):
        
        if ( accl[1] == 0 ):
            return True
        else:
            return False
        
    # mide que no se detecte movimiento en el eje Z
    def situacionZ(self, accl):
        
        if (accl[2] == 0):
            return True
        else:
            return False
        
    def imprimirAccelereacion(self, accl);
        print ("\nX:",accl[0],"\tY:",accl[1],"\tZ:",accl[2])
