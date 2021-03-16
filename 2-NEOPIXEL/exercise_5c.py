from machine import Pin
import neopixel
import time
 
p = neopixel.NeoPixel(Pin(21, Pin.OUT), 1)

def off():
    p[0] = (0, 0, 0)
    p.write()
    
def lightSwitch(ledRange, switchSpeed, wait):
    if (switchSpeed >= ledRange):
        print ("Switch speed can not be equal ot more than ledRange")
        return False
    for a in range(0, ledRange, switchSpeed):
        for b in range(0, ledRange, switchSpeed):
            for c in range(0, ledRange, switchSpeed):
                p[0] = (a, b, c)
                p.write()
                time.sleep_ms(wait)
                
    
# Main code
try:
    # Cycle through the colours
    lightSwitch(50, 49, 50)
    # Put out LED
    off()
except KeyboardInterrupt:
    off()
