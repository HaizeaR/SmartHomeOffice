import time
 
from grove.grove_light_sensor_v1_2 import GroveLightSensor

# import para el sensor 

class Iluminacion():
    
    def __init__(self, puerto):
        self.puerto = puerto 
       
   
    def calcularLuminosidad(self):
        # Grove - Ultrasonic Ranger connected to port D16
        sensor = GroveLightSensor(self.puerto)
        luz = sensor.light
        return luz
    
    # -1 baja la intensidad de la luz
    #  0 todo está bien
    #  1 sube la intensidad de la luz
    def situacionDeLuz(self, luz):
        
        situacion = 0 
        
        if luz < 20:
            situacion = 1
            
        else if luz > 40:
            situacion = -1
        else:
            situacion = 0 
            
        return situacion


