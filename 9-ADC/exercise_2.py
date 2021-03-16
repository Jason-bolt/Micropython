from machine import Pin,DAC,ADC
from time import sleep_ms
import uos

adc = ADC(Pin(35))
adc.atten(ADC.ATTN_11DB)
dac = DAC(Pin(25))

# Checking if data directory exists
try:
    uos.stat("/data")
except OSError:
    print ("/data does not exist, creating it...")
    uos.mkdir('/data')

# Creating the file
file = open("/data/adc.txt", 'w')
# print(dac.write(255))
# print(dac.read())
for i in range(256):
    dac.write(i)
    x = str(adc.read())
    y = str(i)
    file.write(x)
    file.write(" , ")
    file.write(y)
    file.write('\n')
    print(adc.read())
    sleep_ms(2)
    
file.close()