import machine
import time
# import hashlib

uart2=machine.UART(2, baudrate=9600, rx=21, tx=22, timeout=10000)

# print(str(uart2.readline()))
while True:
    if uart2.readline():
        line = uart2.readline()
        print(line)
    print(...)
#     time.sleep(2)