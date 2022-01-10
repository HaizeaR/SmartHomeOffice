import time
 
from grove.grove_light_sensor_v1_2 import GroveLightSensor

# import para el sensor

#Clase relacionada con el sensor de Luz que mide la claridad de la sala
class Iluminacion():
    
    # constructor: se indica el puerto al que se va a conectar el sensor
    def __init__(self, puerto):
        self.puerto = puerto 
       
    # método encargado de leer los valores 
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
        
        if (luz < 300):
            situacion = 1
            
        elif (luz > 600):
            situacion = -1
        else:
            situacion = 0 
            
        return situacion
        
    #Devuelve TRUE cuando la situación no es favorable - se debería encender la bombilla
    #Devuleve FALSE cuando la sitaución es favorable - NO se debería encender la bombilla
    def situacionLuz2(self, luz):
        situacion = False
        
        if(luz < 150):
            situacion = True
        elif(luz > 400):
            situacion = True
        else:
            sitaucion = False
        
        return situacion


