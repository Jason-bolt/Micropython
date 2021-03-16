from machine import Pin, PWM

buzzer = PWM(Pin(18))


buzzer.freq(1000)
buzzer.duty(3000)

# print(buzzer.value())