from machine import Pin, ADC
import time

gas = ADC(Pin(33))

try:
    while True:
        print(gas.read())
        time.sleep_ms(500)
except KeyboardInterrupt:
    print("Done")