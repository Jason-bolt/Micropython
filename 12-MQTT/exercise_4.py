from mqtt import MQTTClient
import network
import time

WIFI_NAME = "DEJJ"
WIFI_PASSWORD = 'Awesomefifa1'
PORT = 1883
HOST = 'mqtt.mydevices.com'
USER_ID = '50457b00-f653-11e9-a38a-d57172a4b4d4'
USER_PASSWORD = 'd02f0fa606e75ca84124ef4564b50c5c292b6886'
CLIENT_ID = '6766e070-3e60-11eb-a2e4-b32ea624e442'
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

payload = "%s,%s=%s" % ('temp', 'c', 12)
msg = 'Send message 1'
while True:
    client.publish(TOPIC, payload)
    print('Sent...')
    time.sleep(2)