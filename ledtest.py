import time
import wiringpi
import sys

def relay1(_pinone):
    wiringpi.digitalWrite(_pinone, 1)
    time.sleep(0.3)
    wiringpi.digitalWrite(_pinone, 0)
    time.sleep(0.3)


def relay2 (_pintwo):
    wiringpi.digitalWrite(_pintwo,1)
    time.sleep(0.3)
    wiringpi.digitalWrite(_pintwo,0)
    time.sleep(0.3)



print ("start")
pinLed1 = 13
pinLed2 = 14
pinSwitch1 = 1
pinSwtich2 = 2
wiringpi.wiringPiSetup()
wiringpi.pinMode(pinLed1, 1)
wiringpi.pinMode(pinLed2, 1)
wiringpi.pinMode(pinSwitch1, 0)
wiringpi.pinMode(pinSwtich2, 0)

while True:
    if(wiringpi.digitalRead(pinSwitch1) == 0):

        relay1(pinLed1)
        print('relay 1 is active')
    elif(wiringpi.digitalRead(pinSwtich2) == 0):
        relay2(pinLed2)
        print('relay 2 is active')
    else: 
        wiringpi.digitalWrite(pinLed1,0)
        wiringpi.digitalWrite(pinLed2,0)
        print('no relay is active')
        time.sleep(1)


print("Done")