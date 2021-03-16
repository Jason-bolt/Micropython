from machine import Pin
import time

def change(pin):
    if (not pin.value()):
        p2.on()
        print("Button clicked!")


pin = Pin(17, Pin.IN, Pin.PULL_UP)
p2 = Pin(2, Pin.OUT)

try:
    while True:
        p2.off()
        change(pin)
        time.sleep_ms(100)
except KeyboardInterrupt:
    print('Exited')
