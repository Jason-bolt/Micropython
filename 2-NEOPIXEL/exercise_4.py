# Change the LED light intensity
from machine import Pin, PWM
import time, math

# Function definitions
def increase(led, rate):
    i = 1
    while i < 1001:
        print(i)
        led.duty(i)
        i = i + rate
        time.sleep_ms(200)
        
def decrease(led, rate):
    i = 1000
    while i >= 0:
        print(i)
        led.duty(i)
        i = i - rate
        time.sleep_ms(200)

def lightControl(led, rate):
    increase(led, rate)
    decrease(led, rate)


#main code
    
try:
    pwm2 = PWM(Pin(2))
    pwm2.freq(1000)
    lightControl(pwm2, 200)
    
except KeyboardInterrupt:
    pwm2.deinit()
    print("Interrupted")