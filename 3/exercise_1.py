from machine import Pin
import time

def change(pin):
    if (not pin.value()):
        print("Button clicked!")


pin = Pin(17, Pin.IN, Pin.PULL_UP)

try:
    while True:
        change(pin)
        time.sleep_ms(100)
except KeyboardInterrupt:
    print('Exited')