
from seeed_dht import DHT


#Clase relacionada con el sensor de Temperatura y humedad

class TemperaturaHumedad():
    # constructor: se indica el puerto al que se va a conectar el sensor
    def __init__(self, puerto):
        self.puerto = puerto
        
    # método encargado de leer los valores 
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
    
    #Devuelve TRUE cuando la situación no es favorable - se debería encender la bombilla
    #Devuleve FALSE cuando la sitaución es favorable - NO se debería encender la bombilla
    def controlTemperatura2(self, temp):
        
        situTemp = False
        # la situación es desfavorable cuado la temperatura es menor que 20 grados o mayor que 22
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
        

    #Devuelve TRUE cuando la situación no es favorable - se debería encender la bombilla
    #Devuleve FALSE cuando la sitaución es favorable - NO se debería encender la bombilla
    def controlHumedad2(self, hum):
        
        situHum = False
        # la situación es desfavorable cuado el % de humedad es menor que 30 grados o mayor que 50
        if (hum < 30):
            situHum = True
        elif (hum > 50):
            situHum = True
        else:
            situHum = False
        
        return situHum 
        
        

        
 


