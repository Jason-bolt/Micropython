#import network
from mqtt import MQTTClient
import machine
import time
import network
from sht3x import SHT3X


WIFI_NAME = "Infinix HOT 6"
WIFI_PASSWORD = "jay123456"
HOST_ID = "192.168.43.192"

try:
    print("Trying to connect to WiFi...")
    while True:        
        wlan = network.WLAN(network.STA_IF)
        #wlan.antenna(WLAN.EXT_ANT)
        wlan.active(True)
        wlan.scan()
        wlan.connect(WIFI_NAME, WIFI_PASSWORD)
        #print("Connected:", wlan.isconnected())
        if (wlan.isconnected()):
            break
        time.sleep(1)
    print("WiFi Connected")
except OSError:
    print("WiFi Connection failed...")
#while not wlan.isconnected(): 
#     machine.idle()


# SHT30 sensor initiation
sensor = SHT3X()

client = MQTTClient("Jason", HOST_ID)
try:
    client.connect()
except OSError:
    print("Can not connect client")

while True:
    try:
        temp, humid = sensor.getTempAndHumi()
        print("Temporature:", temp, 'ºC, RH:', humid, '%')
        msg = (b'{0:3.1f},{1:3.1f}'.format(temp,humid))
        temperature = (b'{0:3.1f}'.format(temp))
        humidity = (b'{0:3.1f}'.format(humid))
        #client.publish(b'test', msg)
        client.publish(b'temperature', temperature)
        client.publish(b'humidity', humidity)
        time.sleep(4)
    except OSError:
        print("Failed...")

    time.sleep(4)
