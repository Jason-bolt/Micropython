# SOS
from machine import Pin
import time

# function for morse S
def morse_s():
    p2 = Pin(2, Pin.OUT)
    p2.on()
    time.sleep_ms(100)
    p2.off()
    time.sleep_ms(100)
    p2.on()
    time.sleep_ms(100)
    p2.off()
    time.sleep_ms(100)
    p2.on()
    time.sleep_ms(100)
    p2.off()
    time.sleep_ms(100)

# function for morse O
def morse_o():
    p2 = Pin(2, Pin.OUT)
    p2.on()
    time.sleep_ms(300)
    p2.off()
    time.sleep_ms(100)
    p2.on()
    time.sleep_ms(300)
    p2.off()
    time.sleep_ms(100)
    p2.on()
    time.sleep_ms(300)
    p2.off()
    time.sleep_ms(100)
    
# function for SOS combining S and O
def sos():
    morse_s()
    morse_o()
    morse_s()
    time.sleep_ms(500)
    
# function for turning the light out when interrupted
def lightOut():
    p2 = Pin(2, Pin.OUT)
    p2.off()


try:
    while True:
        sequence = 2
        while sequence > 0:
            sos()
            sequence = sequence - 1
        time.sleep(1)
except KeyboardInterrupt:
    lightOut()