import time
from grovepi import *
import math


while True:
    try:
        
        accl = acc_xyz()# Get the value from the accelerometer
        
        print ("\nX:",accl[0],"\tY:",accl[1],"\tZ:",accl[2])

    except (IOError,TypeError) as e:
        print("Error")