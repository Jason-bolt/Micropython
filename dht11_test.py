

















#checksum = 0
#for i in range(4):
#    checksum += decodedData[i]
#if checksum != decodedData[4]:
#    print("Chechsum error: expected: 0x%02x but found: 0x%02x"%(decodedData[4],checksum))

#temperature = decodedData[2]+0.1*decodedData[3]
#humidity = decodedData[0]
#print("temperature: %4.1f Â°C, humidity: %d %%"%(temperature,humidity))

#d = 0x007e001f
#mask = 0x80000000

#falseCount = 0
#trueCount = 0

#for j in range(32):
#    print (bin(d)[2:])
#    print (bin(mask)[2:])
#    if (d & mask):
#        print ("True")
#        trueCount += 1
#    else:
 #       print ("False")
 #       falseCount += 1

#    mask >>= 1
    
#print (trueCount)
#print (falseCount)

#d = '0x{:08x}\n'.format(12)

#print (d)