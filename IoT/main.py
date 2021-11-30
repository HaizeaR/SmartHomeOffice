import distance.py
import temp_hum.py
import luz.py

def main():
    
    # INCIALIZAR SENSORES
    # =======================
    d = Distancia(16) # inicializar sensor de ultrasonidos
    
    ht = TemperaturaHumedad(5) #inicializar sensor humedad y temp
    
    l = Iluminacion(0) # inicializar este sensor de luz
    
    
    # CAPTURA DE DATOS
    # ===========================
    
    # mide la distancia 
    distanciaPersona = d.calcularDistancia()
    humtemp = ht.leerValores()
    luz = l.calcularLuminosidad()
    
    
    # indica si esta cerca o lejos (cerca = TRUE)
    estoycerca = errorDistancia(distanciaPersona)

    situacion_humedad = controlTemperatura(humtemp[0])
    situacion_temperatura = controlTemperatura(humtemp[1])

    situacion_luz = situacionDeLuz(luz)
   
    
if __name__ = "__main__":
    main()
