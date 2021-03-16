# Changing the LED color
from machine import Pin
import neopixel
import time

def red(led):
    led[0] = (10, 0, 0)
    led.write()
    
def green(led):
    led[0] = (0, 10, 0)
    led.write()
    
def blue(led):
    led[0] = (0, 0, 10)
    led.write()
 
try:
    led = neopixel.NeoPixel(Pin(21, Pin.OUT), 1)
    while True:
        red(led)
        time.sleep(1)
        green(led)
        time.sleep(1)
        blue(led)
        time.sleep(1)
except KeyboardInterrupt:
    # Turning off the light
    led[0] = (0, 0, 0)
    led.write()
