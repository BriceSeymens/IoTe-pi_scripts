import time
import wiringpi as wp
import sys

print("Start")
trig_pin = 2
echo_pin = 3

# Set the speed of sound in meters per second
speed_of_sound = 343.2

# Set the time for the sensor to settle
settling_time = 0.1

# Set the number of measurements to take
num_measurements = 10

# Set the delay between measurements
measurement_delay = 0.1

# Initialize WiringPi
wp.wiringPiSetup()

# Set the ultrasound emitter pin as output
wp.pinMode(trig_pin, wp.OUTPUT)

# Set the ultrasound sensor pin as input
wp.pinMode(echo_pin, wp.INPUT)

# Loop through the measurements
for i in range(num_measurements):

    # Send the trigger signal
    wp.digitalWrite(trig_pin, wp.LOW)
    time.sleep(settling_time)
    wp.digitalWrite(trig_pin, wp.HIGH)
    time.sleep(0.00001)
    wp.digitalWrite(trig_pin, wp.LOW)

    # Wait for the echo signal
    pulse_start = 0
    pulse_end = 0
    while wp.digitalRead(echo_pin) == wp.LOW:
        pulse_start = time.time()
    while wp.digitalRead(echo_pin) == wp.HIGH:
        pulse_end = time.time()

    # Calculate the distance in meters
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * speed_of_sound / 2.0

    # Print the distance
    print(distance)

    # Wait before taking the next measurement
    time.sleep(measurement_delay)
            