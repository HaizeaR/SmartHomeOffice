import logging
import time
import RPi.GPIO as GPIO
from grove.grove_servo import GroveServo
from distance import Distancia
from temp_hum import TemperaturaHumedad
from luz import Iluminacion
from movimiento import Movimiento

from tb_device_mqtt import TBDeviceMqttClient, TBPublishInfo

thingsboard_server = "thingsboard.cloud"
access_token = "XyuDAUVr1ukFPEoR59HX"


def main():
    
    # Configuration of logger, in this case it will send messages to console
    logging.basicConfig(filename = "/home/pi/Desktop/IoT/smartoffice.log",
                    filemode = 'a',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(module)s - %(lineno)d - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
    '''
    # Grove - Servo connected to PWM port
    servo = GroveServo(12)
    servo_angle = 90
    '''
    
    # INCIALIZAR SENSORES
    # =======================
    #d = Distancia(16) # inicializar sensor de ultrasonidos
    
    ht = TemperaturaHumedad(5) #inicializar sensor humedad y temp
    
    l = Iluminacion(0) # inicializar este sensor de luz
    
    GPIO.setup(22, GPIO.OUT) #Definir el pin 22 como salida del (led/buzzer)
    
    m = Movimiento()
    
    # CONECTARSE A LA PLATAFORMA THINGSBOARD CLOUD
    # ============================================
    
    # Connecting to ThingsBoard
    client = TBDeviceMqttClient(thingsboard_server, access_token)
    #client.set_server_side_rpc_request_handler(on_server_side_rpc_request)
    client.connect()
    # contador utilizado apra calcular si el trabjador se mueve o no, utilizado dentro del método on event
    contador_parada = 0
    
    
    #Método que se encarga de capturar los datos de los sensores y subirlos a la plataforma
    # Se trata de un bucle infinito que ejecuta todas las acciones cada 2 segundos aprox.
    def on_event(contador_parada):

        try:
            #bucle infinito
            while True:
                
                ##CAPTURA DE DATOS
                # =========================================
                # mide la distancia 
                #distanciaPersona = d.calcularDistancia()
                distanciaPersona = 20
                logging.debug('distancia: {} cm'.format(distanciaPersona))

                humtemp = ht.leerValores()
                logging.debug('temperatura: {}C, humedad: {}%'.format(humtemp[1], humtemp[0]))

                situacion_luz = l.calcularLuminosidad()
                logging.debug('luz: {}'.format(situacion_luz))
                
                #situacion_movimiento = m.calcularAceleracion()
                accl  = [0,0,0]
                logging.debug("X: {}   Y: {}  Z: {}".format(accl[0],accl[1],accl[2]))
                
                #TELEMETRY
                #===============================
                # Formatting the data for sending to ThingsBoard
                telemetry = {'distancia': distanciaPersona,
                             'temperatura': humtemp[1],
                             'humedad': humtemp[0],
                             'luz': situacion_luz}

                # Sending the data
                client.send_telemetry(telemetry).get()
                logging.info("Telemetry mandado")                

                #OUTPUTS - LEDS
                #==================================
                situLuz = l.situacionLuz2(situacion_luz)
                GPIO.output(22, situLuz)
                logging.debug('LED luz {}'.format(situLuz))

                #situDistancia = d.errorDistancia(self, distanciaPersona)
                #GPIO.output(23, situDistancia)
                #logging.debug('LED distancia {}'.format(situDistancia))
                
                situTemp = ht.controlTemperatura2(humtemp[0])
                #GPIO.output(24, situDistancia)
                logging.debug('LED temperatura {}'.format(situTemp))
                
                situHum= ht.controlHumedad2(humtemp[1])
                #GPIO.output(25, situDistancia)
                logging.debug('LED humedad {}'.format(situHum))
                
                
                # Esta es otra forma de resolverlo utilizando el otro método
                '''
                if(situLuz == -1 or situLuz == 1):
                    GPIO.output(22, True)
                    print("Led LUZ encencidad")
                    time.sleep(.2)
                else:
                    GPIO.output(22,False)
                    print("Led LUZ apagada")         
            
                '''       
                
                #En este punto se trabaja la funcionalidad de movimiento
                #Este sensor no funciona pero hemos tratado de crear la funcionalidad
                
                situacionParada = m.situacionParada(accl)
                
                if (situacionParada == True):
                    contador_parada = contador_parada + 1 
                else:
                    contador_parada = 0
                    
                    
                if (contador_parada == 60):
                    logger.info("Llevas 5 minutos descansando")
                    contador_parada = 0       
                
                logging.debug('--------------------')
                time.sleep(.2) # mide todo cada x tiempo (2seg)
                
        except Exception as e:
            raise e
            
        finally:
            client.disconnect()
            GPIO.cleanup()
             
    
    on_event(contador_parada)
     
        
if __name__ == "__main__":
    main()
    
    
