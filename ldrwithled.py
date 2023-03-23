import time
import wiringpi
import sys

def ldr(_pinone, _pintwo):

    if (wiringpi.digitalRead(_pinone) == 1):
        wiringpi.digitalWrite(_pintwo, 0)
        print("Light is off")
        time.sleep(0.5)
    else:
        wiringpi.digitalWrite(_pintwo, 1)
        print("Light is on")
        time.sleep(0.5)

print ("start")
pin1 = 1
pin2 = 2
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin1, wiringpi.INPUT)
wiringpi.pinMode(pin2, 1)
while True:

    ldr(pin1, pin2)