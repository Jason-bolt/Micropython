from machine import Pin
import time

button = Pin(17, Pin.IN, Pin.PULL_UP)


while True:
    print(button.value())
    time.sleep_ms(200)
    