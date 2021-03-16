from sht3x import SHT3X

sensor = SHT3X()

sensor.printStatus()

print(sensor.isPresent())

print (bin(sensor.serialNumber()))

print (bin(sensor.readStatus()))

print (sensor.readStatus())

#print (sensor.measPeriodic(noOfMeas=10))
"""
Running the above commented code gives me an empty array
"""

temp, humid = sensor.getTempAndHumi()
print("Temporature:", temp, 'ºC, RH:', humid, '%')

print ("Raw Humidity:", sensor._humi2humiRaw(humid))

print ("Raw Temporature:", sensor._tempC2tempRaw(temp))

print(sensor.readAlert())
