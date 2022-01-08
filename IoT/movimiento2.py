from LSM6DS3 import *
from time import sleep
from grove_rgb_lcd import *
import grovepi

# this is the chip the sensor is based on
mySensor = LSM6DS3()





# let's begin ...
print("GYRO TEST")

# loop forever
while True:

    # print the gyro readings?
    print(mySensor.readRawAccelX(), \
        mySensor.readRawAccelY(), \
        mySensor.readRawAccelZ(), 
          mySensor.calcAnglesXY())
