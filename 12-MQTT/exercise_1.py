from mqtt import MQTTClient
import network
import time

WIFI_NAME = "Infinix HOT 6"
WIFI_PASSWORD = 'jay1234567'
PORT = 1883
HOST = 'mqtt.dioty.co'
USER_ID = 'jappiatu@stu.ucc.edu.gh'
USER_PASSWORD = 'a2375ca4'
CLIENT_ID = 'Jason'
TOPIC = '/jappiatu@stu.ucc.edu.gh/DCSIT'

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
    
    
client = MQTTClient(CLIENT_ID, HOST, port=PORT, user=USER_ID, password=USER_PASSWORD)
try:
    client.connect()
except OSError:
    print("Can not connect client")


msg = 'Send message 1'
while True:
    client.publish(TOPIC, msg)
    print('Sent...')
    time.sleep(2)