import time
import wiringpi
import sys

def lightMeasure(_pinldrone):
    if (wiringpi.digitalRead(pin1) == 1):
        print("light")
        time.sleep(0.5)
    else:
        print("dark")
        time.sleep(0.5)    
    


print ("start")
pin1 = 1
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin1, wiringpi.INPUT)

while True:
    lightMeasure(pin1)