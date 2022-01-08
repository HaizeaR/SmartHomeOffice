# SmartHomeOffice


## Propuesta de proyecto 

La tecnología IoT es la aliada para desarrollar un entorno de trabajo favorable en casa. Los sensores y dispositivos inteligentes pueden insertarse en objetos cotidianos y medir lo que ocurre a nuestro alrededor. La luminosidad de la sala, la temperatura y el ruido ambiente, entre otras cosas, son factores que pueden afectar negativamente al rendimiento de los trabajadores pero pueden ser regulados con facilidad gracias a los actuadores.

Se presenta un sistema que lleva el nombre de Smart Home Office, gracias a una colección de sensores de gran variedad este sistema es capaz de medir las variables básicas para construir un lugar de trabajo saludable. 

### Sensores/Activadores utilizados 

**Sensores:** *(dispositivos capaces de captar magnitudes físicas)*

- Lumiosidad --> medir la intensidad de la luz en el entorno de trabajo
- Temperatura -->
- Humedad --> 
- Distancia -->

**Actuadores:** *(dispositivos capaces de alterar la cantidad física, indicarán al usuario el estado de las variables medidas con los sensores)*

- Led -->
- Buzzer --> 

## Plataforma

ThingsBoard Cloud es una plataforma totalmente gestionada, escalable y tolerante a fallos para aplicaciones IoT. ThingsBoard Cloud es para todos los que quieren usar ThingsBoard pero no quieren alojar su propia instancia de la plataforma y es lo que se utilizará para este proyecto. 

Se utiliza para guardar todos los datos capturados, tener un control sobre ellos, visualizarlos e incluso en ciertos casos avisar mediante alarmas de cualquier error o valor preocupante. 


## FILES 

Este proyecto es una colección de clases, dónde cada una de ellas representa las funcionalidades de cada uno de los sensores y todas ellas se unen en el MAIN.py

El fichero MAIN.py se trata de un bucle que se conecta a la plataforma THINGSBOARD CLOUD, realiza la captura de los datos y se encarga de enviarlos mediante el TELEMETRY. Este no es más que un pequeño string en forma de JSON que envia los últimos valores capturados. 

Este fichero hereda de el resto de clases ya que hace uso de todos los sensores, los conecta, extrae los valores y realiza alguna que otra comparativa. 

### Dependencias y librerias
Para que todo funcione correctamente es necesario instalar ciertos modulos e importar ciertas librerias. 

Todas las clases se ejecutan usando python3. 

- from seeed_dht import DHT
- from grove.grove_light_sensor_v1_2 import GroveLightSensor
- from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
- import RPi.GPIO as GPIO
- from grove.grove_servo import GroveServo
- pip3 install tb-mqtt-client
- from tb_device_mqtt import TBDeviceMqttClient, TBPublishInfo
