from sht30_library import SHT3X

sensor = SHT3X()

print(sensor.isPresent())
temp, humi = sensor.getTempAndHumi()
print("Temporature:", temp, 'ºC, RH:', humi, '%')
tempF = sensor.celcToFarh(temp)
print("Temporature(F):", tempF, "F")
temp, humi = sensor.getTempAndHumi(raw=True)
print("Raw temporature:", temp, ', Raw RH:', humi)
print(sensor.readStatus())
print(sensor.startPeriodicMeasurement())
sensor.stopPeriodicMeasurement()
print(sensor.enableHeater())
print(sensor.disableHeater())
print(sensor.clearAllAlerts())
