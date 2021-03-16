from machine import Pin
import neopixel
import time
 
p = neopixel.NeoPixel(Pin(21, Pin.OUT), 1)

def off():
    p[0] = (0, 0, 0)
    p.write()
    
def lightSwitch(intensity, speed):
    increment = intensity - 1
    for a in range(0, intensity, increment):
        for b in range(0, intensity, increment):
            for c in range(0, intensity, increment):
                p[0] = (a, b, c)
                p.write()
                time.sleep_ms(speed)
                
    
# Main code

try:
    # Cycle through the colours
    lightSwitch(50, 500)
    # Put out LED
    off()
except KeyboardInterrupt:
    off()
