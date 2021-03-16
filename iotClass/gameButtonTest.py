from machine import Pin
import time

top = Pin(17, Pin.IN)
left = Pin(16, Pin.IN)
right = Pin(21, Pin.IN)
bottom = Pin(22, Pin.IN)


# while True:
#     print(top.value())
#     time.sleep_ms(500)



while True:
    if top.value() == 0:
        print("Top pressed!")
    elif left.value() == 0:
        print("Left pressed!")
    elif right.value() == 0:
        print("Right pressed!")
    elif bottom.value() == 0:
        print("Bottom pressed!")
    else:
        print("Waiting!")
    
    time.sleep_ms(500)