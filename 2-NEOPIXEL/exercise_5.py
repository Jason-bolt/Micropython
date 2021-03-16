from machine import Pin
import neopixel
import time
 
p = neopixel.NeoPixel(Pin(21, Pin.OUT), 1)
p[0] = (5, 5, 5)
p.write()