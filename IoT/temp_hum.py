
from seeed_dht import DHT


class TemperaturaHumedad():
    
    def __init__(self, puerto):
        self.puerto = puerto
    
    def leerValores(self):
        sensor = DHT('11', self.puerto)
        humi, temp = sensor.read()
        
        return [humi, temp]
    
    # -1 baja la temperatura
    #  0 todo bien
    #  1 sube la temperatura
    def controlTemperatura(self, temp):
        
        situTemp = 0
        
        if (temp < 20):
            situTemp = 1
        elif (temp > 22):
            situTemp = -1
        
        return situTemp
    
    def controlTemperatura2(self, temp):
        
        situTemp = False
        
        if (temp < 20):
            situTemp = True
        elif (temp > 22):
            situTemp = True
        else:
            situTemp = False
        
        return situTemp
        
    # -1 humedad demasiado alta
    #  0 todo bien
    #  1 humedad demasiado baja  
        
    def controlHumedad(self, hum):
        
        situHum = 0
        
        if (hum < 30):
            situHum = 1
        elif (hum > 50):
            situHum = -1
        
        return situHum 
        

    def controlHumedad2(self, hum):
        
        situHum = False
        
        if (hum < 30):
            situHum = True
        elif (hum > 50):
            situHum = True
        else:
            situHum = False
        
        return situHum 
        
        

        
 


