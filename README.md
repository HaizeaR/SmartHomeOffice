# SmartHomeOffice


## Propuesta de proyecto 

La tecnología IoT es la aliada para desarrollar un entorno de trabajo favorable en casa. Los sensores y dispositivos inteligentes pueden insertarse en objetos cotidianos y medir lo que ocurre a nuestro alrededor. La luminosidad de la sala, la temperatura y el ruido ambiente, entre otras cosas, son factores que pueden afectar negativamente al rendimiento de los trabajadores pero pueden ser regulados con facilidad gracias a los actuadores.

Se presenta un sistema que lleva el nombre de Smart Home Office, gracias a una colección de sensores de gran variedad este sistema es capaz de medir las variables básicas para construir un lugar de trabajo saludable. 

### Sensores/Activadores utilizados 

**Sensores:** *(dispositivos capaces de captar magnitudes físicas)*

- Lumiosidad --> medir la intensidad de la luz en el entorno de trabajo.
- Temperatura --> medir la temperatura de la sala en grados centígrados.
- Humedad --> mide el porcentaje de humedad de la sala.
- Distancia --> mediante ultrasonidos mide la distancia a la que se encuentra el trabajador. 

**Actuadores:** *(dispositivos capaces de alterar la cantidad física, indicarán al usuario el estado de las variables medidas con los sensores)*

- Led --> bombillas de colores que se encienden dadas ciertas condiciones definidias en el código.
- Buzzer --> sonido que se activa dadas ciertas condiciones definidias en el código.

## Plataforma

Para guardar todos los datos capturados, tener un control sobre ellos, visualizarlos e incluso en ciertos casos avisar mediante alarmas de cualquier error o valor preocupante se utiliza la plataforma ThingsBoard Cloud.

ThingsBoard Cloud es una plataforma totalmente gestionada, escalable y tolerante a fallos para aplicaciones IoT. ThingsBoard Cloud es para todos los que quieren usar ThingsBoard pero no quieren alojar su propia instancia de la plataforma y es lo que se utilizará para este proyecto. 

La primera vez que se utilice la plataforma hay que registrarse pero luego se podrá acceder a ella mediante un correo electrónico y contraseña.

## FILES 

Este proyecto es una colección de clases, dónde cada una de ellas representa las funcionalidades de cada uno de los sensores y todas ellas se unen en el MAIN.py. Este fichero hereda de el resto de clases ya que hace uso de todos los sensores, los conecta, extrae los valores y realiza alguna que otra comparativa. 

El fichero MAIN.py se trata de un bucle que se conecta a la plataforma THINGSBOARD CLOUD, realiza la captura de los datos y se encarga de enviarlos mediante el TELEMETRY. Este no es más que un pequeño string en forma de JSON que envia los últimos valores capturados. 

Para una correcta conexión con la plataforma hay dos variables a tener en cuenta, thingsboard_server y access_token. 

- **thingsboard_server**, en nuestro caso al utilizar la versión cloud igualamos a la variable al siguiente string: "thingsboard.cloud"
- **access_token**, es un valor único y aparece dentro del DEVICE creado en la cuenta de thingsboard cloud. 

También hay que tener en cuenta que se creará un fichero .log con el nombre de 'smartoffice.log', en el que se guardará el historial de ejecución puediendo tener una herramienta para visibilizar cualquier error o situación no deseada. 

### Dependencias y librerias
Para que todo funcione correctamente es necesario instalar ciertos modulos e importar ciertas librerias. 

Todas las clases se ejecutan usando **python3**. 

Para hacer uso de las funcionalidades de los sensores es necesario instalar estas librerias: 
- pip3 install grove.py 
- pip3 install seeed-python-dht

Para poder hacer uno de del acelerometro es necesario instalar la siguiente libreria: 
- pip3 install grovepi

Es necesario ejecutar el siguiente comando en la terminal para poder acceder a los módulos de tb_device_mqtt:
- pip3 install tb-mqtt-client

Gracias a este install funcionará correctamente la conexión a thingsboardCloud


## Otros ficheros 

A parte del código esencial para la ejecución encontramos otras dos carpetas con más contenido

### Extras

En la carpeta extras se encuentra un fichero con el nombre de sample.service, contiene información sobre cómo gestionar la aplicación, incluyendo cómo iniciar o detener el servicio y cuándo debe iniciarse automáticamente, en este caso al arrancar la Raspberry. 

En la siguiente página se muestra paso por paso como se hace uso de este .service {https://domoticproject.com/creating-raspberry-pi-service/}

### Jsons

Contiene los Jsons que replican los Dashboards que se encontrarán en la plataforma. 

- SmartOffice -> muestra los datos capturados por el sensor. 
- SmartOfficeAnálisis -> muestra un historico del sensor mediante el cual se pueden hacer pequeños análisis.
- SmartOfficeAnálisisGeneral -> muestra un resumen histórico de los datos de varios devices. 

### creargrupo.py

Este fichero es independiente del resto de clases, en este se intenta crear una REST API mediante la cual se creen grupos de clientes, devices, dashboards compartidos y se creen nuevos usuarios. La idea de este fichero es ser capaz de automatizar por código funcionalidades clave de la plataforma Thingsboard cloud. Este fichero solo se debería ejecutar una única vez y así crear todos los componentes definidos en el mismo, ahorrandonos la necesidad de crearlos a mano.


---------
Si es la primera vez que haces uso de una Raspberry Pi puedes mirar en este enlace información sobre sus sensores básicos y ejemplos de como utilizarlos: https://wiki.seeedstudio.com/Grove_Base_Kit_for_Raspberry_Pi/ 

> Recuerda establecer una conexión a internet mediante cable o red wifi. 


