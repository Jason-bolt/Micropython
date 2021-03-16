from machine import Pin, I2C

def measure():
    """
    If raw==True returns a bytearrya(6) with sensor direct measurement otherwise
    It gets the temperature (T) and humidity (RH) measurement and return them.
    
    The units are Celsius and percent
    """
    
    jason.writeto(0x45, b'\x2C\x10')
    data = jason.readfrom(0x45, 6) 

    """
    t_celsius = (((data[0] << 8 |  data[1]) * 175) / 0xFFFF) - 45
    rh = (((data[3] << 8 | data[4]) * 100.0) / 0xFFFF)
    return t_celsius, rh

    #return data
    """
    
    aux = (data[0] << 8 | data[1]) * 175
    t_int = (aux // 0xffff) - 45;
    t_dec = (aux % 0xffff * 100) // 0xffff
    aux = (data[3] << 8 | data[4]) * 100
    h_int = aux // 0xffff
    h_dec = (aux % 0xffff * 100) // 0xffff
    return t_int, t_dec, h_int, h_dec
    
    

jason = I2C(1, scl=Pin(22), sda=Pin(21))

device = jason.scan()

register = hex(device[0])

measurement = measure()
temp = str(measurement[0]) + '.' + str(measurement[1])
humid = str(measurement[2]) + '.' + str(measurement[3])

print("Temperature: ", temp)
print("Humidity: ", humid)