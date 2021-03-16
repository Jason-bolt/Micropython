from sht3x import SHT3X

sensor = SHT3X()

#print(sensor.isPresent())

#print (bin(sensor.serialNumber()))

#print (bin(sensor.readStatus()))

#print (sensor.readStatus())

sensor.printStatus()

#print (sensor.measPeriodic(noOfMeas=10))

#temp, humid = sensor.getTempAndHumi()
#print("Temporature:", temp, 'ºC, RH:', humid, '%')