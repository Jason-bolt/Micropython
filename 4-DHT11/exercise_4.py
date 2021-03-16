import sys

# Opening the source file
s_file = open("/data/rawDht11.txt", "r")

# Opening destination file
d_file = open("/data/unpacked.txt", "w")

# Looping through the file to access hex numbers
for i in range(32):
    # Get hex number
    hex_number = int(s_file.readline(), 16)
    #print ("Number: %08x"%hex_number)
    # Mask number
    mask = 0x80000000
    for j in range(32):
        if (hex_number & mask):  # if mask 'on' position is on in hex_number
            d_file.write("1\n")
        else:  # if mask 'on' is off in hex_number
            d_file.write("0\n")
        mask >>= 1 # shift mask bit
        
s_file.close()
d_file.close()


