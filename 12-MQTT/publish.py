from umqtt.simple import MQTTClient
import network
import time
from wifi_connect import *

SERVER = "192.168.43.1"
TOPIC = b"DCSIT"
PAYLOAD = b"Welcome to the DCSIT IoT course"
WIFI_NAME = "Infinix HOT 6"
WIFI_PASSWORD = "jay1234567"


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


# connect()

c = MQTTClient("umqtt_client", SERVER)
c.connect()

for i in range(0, 10):
    c.publish(TOPIC, PAYLOAD)
    print("Sent...")
    time.sleep(1)
c.disconnect()