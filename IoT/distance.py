# import para el sensor 
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger

class Distancia():
    
    def __init__(self, puerto):
        self.puerto = puerto 
       
    
    def calcularDistancia(self):
        # Grove - Ultrasonic Ranger connected to port D16
        sensor = GroveUltrasonicRanger(self.puerto)
        distance = sensor.get_distance()
        return distance
    
    #TRUE significa que hay algo mal que se tiene que cambiar 
    def errorDistancia(self, distance):
        
        if (distance <= 65):
            return True
        
        return False


