import machine
import time
 
interruptCounter = 0
totalInterruptsCounter = 0
 
def callback(pin):
  global interruptCounter
  interruptCounter = interruptCounter+1
 
p17 = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_UP)
 
p17.irq(trigger=machine.Pin.IRQ_FALLING, handler=callback)

try:
    while True:
        if (interruptCounter > 0):
            state = machine.disable_irq()
            interruptCounter = interruptCounter-1
            machine.enable_irq(state)

            totalInterruptsCounter = totalInterruptsCounter+1
            print("Interrupt has occurred: " + str(totalInterruptsCounter))
        time.sleep_ms(100)
            
except KeyboardInterrupt:
    print("Exited")