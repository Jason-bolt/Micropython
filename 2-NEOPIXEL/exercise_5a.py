from machine import Pin
import neopixel
import time
 
p = neopixel.NeoPixel(Pin(21, Pin.OUT), 1)

def off():
    p[0] = (0, 0, 0)
    p.write()
    

off()