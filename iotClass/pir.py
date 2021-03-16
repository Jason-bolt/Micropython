from machine import Pin
import time

pir = Pin(22, Pin.IN)

while True:
    print(pir.value())
    time.sleep_ms(500)
