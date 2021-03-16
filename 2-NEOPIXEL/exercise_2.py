# The blinking LED
from machine import Pin, PWM

try:
    while True:
        pwm2 = PWM(Pin(2), freq=1, duty=500)
except KeyboardInterrupt:
    pwm2.deinit()
    print("Interrupted")
