from machine import Pin, PWM
import time

led = Pin(2, Pin.OUT)
pir = Pin(17, Pin.IN, Pin.PULL_UP)
buzpin = Pin(18,Pin.OUT)
buzzer = PWM(buzpin)
buzzer.deinit()

def pirsensor(pir):    
    pirState = pir.value()
    print(pirState)
#     time.sleep_ms(200)
    if pirState == 1:
        led.value(1)
        sos()
#         buzzer.freq(500)
#         buzzer.duty(100)
#         time.sleep(1)
        buzzer.duty(0)

        print('detected')
    else:
        led.off()
        
def sos():
    for note in range(0,9):
        if note == 3 or note == 4 or note == 5:
            buzzer.init()
            buzzer.freq(2000)
            buzzer.duty(200)
            time.sleep_ms(200)       
        else:
            buzzer.freq(1000)
            #time.sleep_ms(200)
            buzzer.duty(200)
            time.sleep_ms(200)
            buzzer.duty(0)     
    buzzer.duty(0)
    buzzer.deinit()


pir.irq(trigger=3, handler=pirsensor)
# while True:
#     print(pir.value())
#     time.sleep_ms(500)