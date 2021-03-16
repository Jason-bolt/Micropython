import sys


"""
STEPS

1. Open the file (It has 32 hex numbers of which each can be represented as a 32 bit number)
2. For each hex number find the number of high bits in a sequence(pulse) and put them in an array
    (It sould be 40 pulses)
    # Each pulse is either a high or a low
3. Assign '1' to highs (preferrably values above 10) and assign '0' to lows (values below 10)
    
    # Bit assignment
        -> First 8 is humidity whole value
        -> Second 8 is humidity decimal value
        -> Third 8 is temperature whole value
        -> Fourth 8 is temperature decimal value
        -> Fifth 8 is checksum
        
    # Checksum must be equal to the summation of first 32 bits
"""

# Defining variables
bitCount = 0
bits = []


# Opening the file
file = open("/data/rawDht11.txt", "r")

# Looping through the file to access hex numbers
for i in range(32):
    # Get hex number
    hex_number = int(file.readline(), 16)
    #print ("Number: %08x"%hex_number)
    # Mask number
    mask = 0x80000000
    for j in range(32):
        if (hex_number & mask):  # if mask 'on' position is on in hex_number
            bitCount += 1
            #print(bitCount)
        else:  # if mask 'on' is off in hex_number
            # print (bitCount)
            if bitCount > 0:
                bits.append(bitCount)
            bitCount = 0
        mask >>= 1 # shift mask bit
        
file.close()

NumOfPulses = len(bits)

if NumOfPulses != 40:
    print ("Error in code logic!")
    sys.exit(-1)
    

# New array containing the 5 numbers from the 40 bit sequence
values_array = []

for i in range(5):
    # number after working every 8 bit sequence
    num = 0
    for j in range(8):
        if (bits[i * 8 + j] > 10):
            num = num | 1  # Turns the last bit in num into a '1'
        if j < 7:
            num = num << 1  # Shift bits to the left by adding a '0' to the right end
    # Appending the values
    values_array.append(num)
    
#print (values_array)

# Checking if checksum value matches
checkSum = 0
for i in range(4):
    checkSum += values_array[i]
if checkSum != values_array[4]:
    print ("Checksum value is not correct")
else:
    humidityWhole = values_array[0]
    humidityDec = values_array[1]
    humidity = str(humidityWhole) + "." + str(humidityDec) + "%"
    #print (humidity)
    temporatureWhole = values_array[2]
    temporatureDec = values_array[3]
    temporature = str(temporatureWhole) + "." + str(temporatureDec) + "°C"
   # print (temporature)
    print ("Humidity = ", humidity, "\nTemporature = ", temporature)

