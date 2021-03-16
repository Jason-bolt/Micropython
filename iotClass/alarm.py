#using PIR SENSOR to detect motion and triger an alarm and on a led

from machine import Pin,PWM
import time

led = Pin(2,Pin.OUT)
pin5 = 17
pir = Pin(pin5, Pin.IN, Pin.PULL_UP)
pin=18
buzpin = Pin(pin,Pin.OUT)
buzzer = PWM(buzpin)




# def sos():
#     led.value(1)
#     for note in range(0,9):
#         if note == 3 or note == 4 or note == 5:
#             buzzer.freq(2000)
#             buzzer.duty(200)
#             time.sleep_ms(200)
#             
#         else:
#             buzzer.freq(1000)
#             #time.sleep_ms(200)
#             buzzer.duty(200)
#             time.sleep_ms(200)
#             buzzer.duty(0)
#         
#     buzzer.duty(0)
#     buzzer.deinit()
#     led.value(0)
    
    
    
def pirsensor(pir):    
    pirState = pir.value()
    print(pirState)
    time.sleep_ms(200)
    if pirState == 1:
        led.value(1)
        print('Heat signature detected')
#         sos()
#         buzzer.freq(500)
#         buzzer.duty(100)
#         time.sleep(1)
#         buzzer.duty(0)

        print('detected')
    else:
        led.off()
        
pir.irq(trigger=3, handler=pirsensor)#Pin.IRQ_FALLING



# try:
#     #pir.irq(trigger=3, handler=pirsensor)#Pin.IRQ_FALLING
#     while True:
#         #sos()
#         pirsensor(pir)
#     
# except KeyboardInterrupt:
#     print('Ended')
    

