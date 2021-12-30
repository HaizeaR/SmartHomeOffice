import logging
import time
import RPi.GPIO as GPIO
from grove.grove_servo import GroveServo
from distance import Distancia
from temp_hum import TemperaturaHumedad
from luz import Iluminacion
from tb_device_mqtt import TBDeviceMqttClient, TBPublishInfo


# Configuration of logger, in this case it will send messages to console
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(module)s - %(lineno)d - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

log = logging.getLogger(__name__)

thingsboard_server = "thingsboard.cloud"
access_token = "vdN4FuEf0yErZN8sScLF"


def main():
    
    # Grove - Servo connected to PWM port
    servo = GroveServo(12)
    servo_angle = 90
    
    # INCIALIZAR SENSORES
    # =======================
    #d = Distancia(16) # inicializar sensor de ultrasonidos
    
    ht = TemperaturaHumedad(5) #inicializar sensor humedad y temp
    
    l = Iluminacion(0) # inicializar este sensor de luz
    
    GPIO.setup(22, GPIO.OUT) #Definir el pin 22 como salida del (led)
    
    # Callback for server RPC requests (Used for control servo and led blink)
    def on_server_side_rpc_request(client, request_id, request_body):
        log.info('received rpc: {}, {}'.format(request_id, request_body))
        if request_body['method'] == 'getLedState':
            client.send_rpc_reply(request_id, light_state)
        elif request_body['method'] == 'setLedState':
            light_state = request_body['params']
            button.led.light(light_state)
        elif request_body['method'] == 'setServoAngle':
            servo_angle = float(request_body['params'])
            servo.setAngle(servo_angle)
        elif request_body['method'] == 'getServoAngle':
            client.send_rpc_reply(request_id, servo_angle)

    # Connecting to ThingsBoard
    client = TBDeviceMqttClient(thingsboard_server, access_token)
    #client.set_server_side_rpc_request_handler(on_server_side_rpc_request)
    client.connect()
    
    
    
    def on_event():

        try:
            while True:
                # mide la distancia 
                #distanciaPersona = d.calcularDistancia()
                distanciaPersona = 20
                log.debug('distancia: {} cm'.format(distanciaPersona))

                humtemp = ht.leerValores()
                log.debug('temperatura: {}C, humedad: {}%'.format(humtemp[0], humtemp[1]))

                situacion_luz = l.calcularLuminosidad()
                log.debug('luz: {}'.format(situacion_luz))

                # Formatting the data for sending to ThingsBoard
                telemetry = {'distancia': distanciaPersona,
                             'temperatura': humtemp[1],
                             'humedad': humtemp[0],
                             'luz': situacion_luz}

                # Sending the data
                client.send_telemetry(telemetry).get()
                
                situTemp = ht.controlTemperatura(humtemp[0])
                situHum= ht.controlHumedad(humtemp[1])
              
                situLuz = l.situacionDeLuz(situacion_luz)
                print(situLuz)
                if(situLuz== -1):
                    GPIO.output(22, True)
                    print("Entr")
                    time.sleep(.2)
                else:
                    GPIO.output(22,False)
                
                
                time.sleep(.10) # mide todo cada x tiempo (2seg)
                

                
        except Exception as e:
            raise e
            
        finally:
            client.disconnect()
            GPIO.cleanup()
        
        return [situTemp, situHum]

    on_event()
  
        
        
if __name__ == "__main__":
    main()
    
    
