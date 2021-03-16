from machine import Pin,DAC,ADC
import time

Yadc = ADC(Pin(35))  # For the y axis
Xadc = ADC(Pin(33))  # For the x axis
Yadc.atten(ADC.ATTN_11DB)
Xadc.atten(ADC.ATTN_11DB)

for i in range(200):
    print("Ver:", Yadc.read())
    print("Hor:", Xadc.read())
    time.sleep(1)


