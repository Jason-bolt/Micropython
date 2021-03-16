from machine import Pin, ADC
import time

pot = ADC(Pin(33))
pot.atten(ADC.ATTN_11DB)

while True:
    print(pot.read())
    time.sleep_ms(200)