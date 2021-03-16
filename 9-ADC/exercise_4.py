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
file = open("/data/adc_corrected.txt", 'w')
# print(dac.write(255))
# print(dac.read())
for i in range(256):
    dac.write(i)
    j = adc.read()
    fit = (-3.52345557e-32 * (j**10)) + (7.76924569e-28 * (j**9)) + (-7.24592566e-24 * (j**8)) + (3.72369972e-20 * (j**7)) + (-1.15046054e-16 * (j**6)) + (2.18797204e-13 * (j**5))+ (-2.53284539e-10 * (j**4)) + (1.73568654e-07 * (j**3)) + (-6.94061397e-05 * (j**2)) + (  8.23528583e-02 * j) + 1.82308867e+00
#     x = str(0.06414 * adc.read() + 5.986)
    x = str(fit)
    y = str(i)
    file.write(x)
    file.write(" , ")
    file.write(y)
    file.write('\n')
    print(adc.read())
    sleep_ms(2)
    
file.close()
