import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

wlan.connect("Infinix HOT 6", "jay1234567")

for _ in range(100):
    print(wlan.isconnected())