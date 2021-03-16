from machine import Pin, PWM
import time

# LED 1 = 27 Green
# LED 2 = 25 Red
# LED 3 = 32 Green 2
# LED 4 = 22 Orange
# LED 5 = 21 White
# LED 6 = 17 Black
# LED 7 = 16 White 2
# LED 8 = 26 White 3

# Button = 18

led1 = PWM(Pin(27))
led2 = PWM(Pin(25))
led3 = PWM(Pin(32))
led4 = PWM(Pin(22))
led5 = PWM(Pin(21))
led6 = PWM(Pin(17))
led7 = PWM(Pin(16))
led8 = PWM(Pin(26))

button = Pin(18, Pin.IN)



def lightSwitch(speed, but):
    
    led1.duty(0)
    led2.duty(0)
    led3.duty(0)
    led4.duty(0)
    led5.duty(0)
    led6.duty(0)
    led7.duty(0)
    led8.duty(0)
    
    
#     while speed >= 0:
    while True:
        print(speed)
        
        led1.duty(300)
        time.sleep_ms(speed)
        led1.duty(0)
        
        led2.duty(300)
        time.sleep_ms(speed)
        led2.duty(0)
        
        led3.duty(300)
        time.sleep_ms(speed)
        led3.duty(0)
        
        led4.duty(300)
        if but.value() == 0:
            time.sleep(2)
        time.sleep_ms(speed)
        led4.duty(0)
        
        led5.duty(300)
        time.sleep_ms(speed)
        led5.duty(0)
        
        led6.duty(300)
        time.sleep_ms(speed)
        led6.duty(0)
        
        led7.duty(300)
        time.sleep_ms(speed)
        led7.duty(0)
        
        led8.duty(300)
        time.sleep_ms(speed)
        led8.duty(0)
        
#         speed -= 20


lightSwitch(100, button)
    