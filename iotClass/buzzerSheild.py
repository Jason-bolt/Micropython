from machine import Pin, PWM
import time

buz = PWM(Pin(18, Pin.OUT))

def doReMi():
    buz.freq(261)
    time.sleep_ms(500)
    buz.duty(0)
    time.sleep_ms(500)
    
    buz.duty(300)
    buz.freq(293)
    time.sleep_ms(500)
    buz.freq(329)
    time.sleep_ms(500)
    buz.freq(349)
    time.sleep_ms(500)
    buz.freq(392)
    time.sleep_ms(500)
    buz.freq(440)
    time.sleep_ms(500)
    buz.freq(493)
    time.sleep_ms(500)
    buz.freq(523)
    time.sleep_ms(500)

while True:
    doReMi()