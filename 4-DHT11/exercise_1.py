from dht import DHT11
from machine import Pin
import time


def dht_value():
    dht11 = DHT11(Pin(16))
    dht11.measure()
    return ('Temperature = ', dht11.temperature(), ' Humidity = ', dht11.humidity())


while (True):
    print (dht_value())
    time.sleep(2)
