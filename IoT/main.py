import logging
import time
from grove.grove_servo import GroveServo
from distance import Distancia
from temp_hum import TemperaturaHumedad
from luz import Iluminacion

# Configuration of logger, in this case it will send messages to console
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(module)s - %(lineno)d - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

log = logging.getLogger(__name__)

thingsboard_server = 'd8ac2bb0-5394-11ec-92b4-a78618b86b39'
access_token = 'hMJ9iPzRcjZNClVdkKEj'


def main():
    
    # Grove - Servo connected to PWM port
    servo = GroveServo(12)
    servo_angle = 90
    
    # INCIALIZAR SENSORES
    # =======================
    d = Distancia(16) # inicializar sensor de ultrasonidos
    
    ht = TemperaturaHumedad(5) #inicializar sensor humedad y temp
    
    l = Iluminacion(0) # inicializar este sensor de luz
    
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
    client.set_server_side_rpc_request_handler(on_server_side_rpc_request)
    client.connect()
    
 
    # Callback on detect the motion from motion sensor
    def on_detect():
        log.info('motion detected')
        telemetry = {"motion": True}
        client.send_telemetry(telemetry)
        time.sleep(5)
        # Deactivating the motion in Dashboard
        client.send_telemetry({"motion": False})
        log.info("Motion alert deactivated")
    
    
    
      def on_event():

        try:
            while True:
                # mide la distancia 
                distanciaPersona = d.calcularDistancia()
                log.debug('distancia: {} cm'.format(distanciaPersona))

                humtemp = ht.leerValores()
                log.debug('temperatura: {}C, humedad: {}%'.format(humtemp[0], humtemp[1]))

                situacion_luz = l.situacionDeLuz(luz)
                log.debug('luz: {}'.format(situacion_luz))

                # Formatting the data for sending to ThingsBoard
                telemetry = {'distancia': distanciaPersona,
                             'temperatura': humtemp[0],
                             'humedad': humtemp[1],
                             'luz': situacion_luz}

                # Sending the data
                client.send_telemetry(telemetry).get()

                time.sleep(.1)
        except Exception as e:
            raise e
        finally:
            client.disconnect()
        

        
if __name__ == "__main__":
    main()
