import time
import wiringpi
import sys

def fullStepLeft(_pinone,_pintwo,_pinthree,_pinfour):
    wiringpi.digitalWrite(_pinfour, 0)
    wiringpi.digitalWrite(_pintwo, 1)
    time.sleep(0.01)
    wiringpi.digitalWrite(_pinone, 0)
    wiringpi.digitalWrite(_pinthree, 1)
    time.sleep(0.01)
    wiringpi.digitalWrite(_pintwo, 0)
    wiringpi.digitalWrite(_pinfour, 1)
    time.sleep(0.01)
    wiringpi.digitalWrite(_pinthree, 0)
    wiringpi.digitalWrite(_pinone, 1)

def fullStepRight(_pinone,_pintwo,_pinthree,_pinfour):
    wiringpi.digitalWrite(_pinfour, 1)
    wiringpi.digitalWrite(_pintwo, 0)
    time.sleep(0.01)
    wiringpi.digitalWrite(_pinone, 1)
    wiringpi.digitalWrite(_pinthree, 0)
    time.sleep(0.01)
    wiringpi.digitalWrite(_pintwo, 1)
    wiringpi.digitalWrite(_pinfour, 0)
    time.sleep(0.01)
    wiringpi.digitalWrite(_pinthree, 1)
    wiringpi.digitalWrite(_pinone, 0)



print ("start")
pinLed1 = 1
pinLed2 = 2
pinLed3 = 3
pinLed4 = 4
wiringpi.wiringPiSetup()
wiringpi.pinMode(pinLed1, 1)
wiringpi.pinMode(pinLed2, 1)
wiringpi.pinMode(pinLed3, 1)
wiringpi.pinMode(pinLed4, 1)


while True:
   fullStepRight(pinLed1,pinLed2,pinLed3,pinLed4)

print("Done")