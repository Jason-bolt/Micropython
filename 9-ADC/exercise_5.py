from machine import Pin,DAC,ADC
from time import sleep_ms
import math
import uos
PI = math.pi

adc = ADC(Pin(35))
adc.atten(ADC.ATTN_11DB)
dac = DAC(Pin(25))

# Saw tooth graph
def saw_tooth(waveCount=None):
    if waveCount == None:
        waveCount = 5
    for _ in range(waveCount):
        for i in range(256):
            dac.write(i)
            print(i)
            print(adc.read())
            sleep_ms(2)

# Rectangular graph
def rect(waveCount=None, length=None):
    if length == None:
        length = 3
    if waveCount == None:
        waveCount = 5
    for _ in range(waveCount):
        for a in range(length):
            i = 0
            print(i)
        for a in range(length):
            i = 255
            print(i)
    
# Triangular graph
def triangle(waveCount=None):
    if waveCount == None:
        waveCount = 5
    for _ in range(waveCount):
        for i in range(256):
            dac.write(i)
            print(i)
#             print(adc.read())
            sleep_ms(2)
        for g in range(255, 0, -1):
            dac.write(g)
            print(g)
#             print(adc.read())
            sleep_ms(2)

# sine graph
def sine(waveCount=None):
    if waveCount == None:
        waveCount = 5
    for a in range(waveCount):
        angle90 = PI/2
        dac.write(int(math.radians(angle90 * a)))
        angle = math.sin(math.radians(angle90 * a))
        print(math.radians(angle90 * a))
        print(angle)
        
        
sine()