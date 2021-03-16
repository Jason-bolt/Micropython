from hcsr04 import HCSR04
import time
from machine import Pin

sensor = HCSR04(trigger_pin=18, echo_pin=26, echo_timeout_us=1000000)
motor = Pin(16, Pin.OUT)

# Set motor to off
motor.off()

while True:
    # Get distance in centimeters from the ultrasonic sensor
    distance = sensor.distance_cm()
    # Display distance
    print(distance)
    # Delay for 100 miliseconds
    time.sleep_ms(100)
    
    # Checking if distance is less than 4cm
    if distance <= 19:
        # Turn on motor
        motor.on()
        # Delay for 5 seconds
        time.sleep(5)
    # Turn off motor
    motor.off()