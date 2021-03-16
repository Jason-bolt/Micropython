import sht30
from machine import Pin, I2C

i2c = I2C(scl=Pin(26), sda=Pin(18), freq = 400000)

def PrintAddresses():
    address = i2c.scan()   # To get the address of slaves on the I2C bus
    new = hex(address[0])
    newList = list(new)
    #print(newList[0])
    top = 0
    topa = 'a'
    left = 0
    lefta = 'a'
    for i in range(0, 17):        #For rows
        print ('\n')               # Break the line for each row
        for j in range(0, 16):       # For columns
            if (i == 0):           # Selecting the first row
                if (j == 0):             # Selecting the first coloumn
                    print (' ', end = '')
                    print (' ', end = '')
                    print (' ', end = '')
                    print (' ', end = '')    # Giving space before first column
                if (top < 10):
                    print (' ', end = '')
                    print (top, end = '')
                    print (' ', end = '')
                    top = top + 1
                else:
                    print (' ', end = '')
                    print (topa, end = '')
                    print (' ', end = '')
                    temp = ord(topa[0]) + 1
                    topa = chr(temp)
                
            else:
                if (j == 0):
                    if (left < 10):
                        temp1 = str(left) + '0:'
                        print(temp1, end = '')
                        print (' ', end = '')
                        #int(left)
                        left = left + 1
                        
                    else:
                        temp2 = lefta + '0:'
                        print (temp2, end = '')
                        print (' ', end = '')
                        temp = ord(lefta[0]) + 1
                        lefta = chr(temp)
                
                if (i == int(newList[-2]) + 1 and j == int(newList[-1])):
                #if (top == 5):
                    number = str(int(newList[-2])) + str(int(newList[-1]))
                    #print (' ', end = '')
                    print (number, end = '')
                    print (' ', end = '')
                else:
                    print ('__ ', end = '')
                


#PrintAddresses()

#address = i2c.scan()
#new = hex(address[0])
#newList = list(new)
#print(newList[-2])

#bytelist = b'\x2C\x10'
#bytelist = b'\xff\xff\xff'
#print(int.from_bytes(b'\x00\x11', "big"))
#for b in bytelist:
#    print(b)
#print (bytelist[:-1])

print(i2c.scan())
#i2c.writeto(0x45, b'\x2D\x10')
print(i2c.readfrom(0x45, 6))
