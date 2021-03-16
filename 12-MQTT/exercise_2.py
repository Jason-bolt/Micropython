import paho.mqtt.client as mqtt
import time

# Define event callbacks
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully.")
        # global connected
        # connected = True
        mqttclient.subscribe(TOPIC)

    else:
        print("Connection failed. rc= "+str(rc))

def on_publish(client, userdata, mid):
    print("Message "+str(mid)+" published.")

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribe with mid "+str(mid)+" received.")

def on_message(client, userdata, msg):
    # Messagereceived = True
    print("Message received " + str(msg.payload.decode("utf-8")))
    print("Topic" + str(msg.topic))

USER_NAME = 'jappiatu@stu.ucc.edu.gh'
USER_PASSWORD = 'a2375ca4'
HOST_NAME = 'mqtt.dioty.co'
PORT = 1883
TOPIC = "/jappiatu@stu.ucc.edu.gh/DCSIT"

mqttclient = mqtt.Client('Jason')
mqttclient.username_pw_set(USER_NAME, password=USER_PASSWORD)
mqttclient.connect(HOST_NAME, PORT, 60)


while True:
    mqttclient.on_connect = on_connect
    mqttclient.on_message = on_message
    mqttclient.loop_forever()
