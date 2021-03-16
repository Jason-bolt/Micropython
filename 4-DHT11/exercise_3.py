import uos
import array
import dht11Raw
from machine import Pin

# Defining pin
pin = Pin(16)

# Checking if the file exists
try:
    uos.stat('/data')
except OSError:
    print ("/data does not exist, creating it...")
    uos.mkdir('/data')
    
# creating array for raw data
dht11Data = array.array("I",[0]*32) # I represents unsigned integer. The array is filled with 32 0s

# Putting data into dht11Data array
dht11Raw.dht11ReadRaw(pin, dht11Data)

# Creating file with raw data calling it rawDht11
file = open("/data/rawDht11.txt", "w")

# Writing hex formatted values in text file
for i in range(32):
    # 0x{:08x} format so that numbers can be represented as 32 bit numbers
    hexFormat = "0x{:08x}\n".format(dht11Data[i])
    file.write(hexFormat)
    print (hexFormat)
    
# Closing file
file.close()