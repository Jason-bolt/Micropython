import sys
import matplotlib.pyplot as plt

#print("Unpacking DHT11 data")
try:
    file = open("dht11.txt","r")
except:
    print("Could not open the file 'dht11.txt' for reading, giving up ...")
    sys.exit()

bits=[]
x=range(0,1024*4,4)
print(x)
for i in range(32):
    d=int(file.readline(),16)
#    print("value read: %08x"%d)
    mask = 0x80000000
    for j in range(32):
        if d & mask:
            bits.append(1)
        else:
            bits.append(0)
        mask = mask >> 1

file.close()
print("bits length: %d"%len(bits))
fig, ax = plt.subplots(figsize=(15,5))
ax.set(xlabel='time (us)', ylabel='signal level',
       title='DHT11 protocol')
ax.plot(x,bits)
ax.grid()

plt.show()



