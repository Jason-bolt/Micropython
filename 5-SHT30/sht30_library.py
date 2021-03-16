"""
Project: SHT3X library
Author: Jason Kwame Appiatu
Date: 18th July, 2020

"""

# importing needed libraries
import sys
from machine import Pin,I2C
import time


class SHT3X:
    # Defining constants
    POLYNOMIAL = 0x31
    
    CMD_READ_SERIALNBR  = b'\x37\x80' # read serial number
    CMD_READ_STATUS     = b'\xF3\x2D' # read status register
    CMD_CLEAR_STATUS    = b'\x30\x41' # clear status register
    CMD_HEATER_ENABLE   = b'\x30\x6D' # enabled heater
    CMD_HEATER_DISABLE  = b'\x30\x66' # disable heater
    CMD_SOFT_RESET      = b'\x30\xA2' # soft reset
    CMD_MEAS_CLOCKSTR_H = b'\x2C\x06' # measurement: clock stretching, high repeatability
    CMD_MEAS_CLOCKSTR_M = b'\x2C\x0D' # measurement: clock stretching, medium repeatability
    CMD_MEAS_CLOCKSTR_L = b'\x2C\x10' # measurement: clock stretching, low repeatability
    CMD_MEAS_POLLING_H  = b'\x24\x00' # measurement: polling, high repeatability
    CMD_MEAS_POLLING_M  = b'\x24\x0B' # measurement: polling, medium repeatability
    CMD_MEAS_POLLING_L  = b'\x24\x16' # measurement: polling, low repeatability
    CMD_MEAS_PERI_05_H  = b'\x20\x32' # measurement: periodic 0.5 mps, high repeatability
    CMD_MEAS_PERI_05_M  = b'\x20\x24' # measurement: periodic 0.5 mps, medium repeatability
    CMD_MEAS_PERI_05_L  = b'\x20\x2F' # measurement: periodic 0.5 mps, low repeatability
    CMD_MEAS_PERI_1_H   = b'\x21\x30' # measurement: periodic 1 mps, high repeatability
    CMD_MEAS_PERI_1_M   = b'\x21\x26' # measurement: periodic 1 mps, medium repeatability
    CMD_MEAS_PERI_1_L   = b'\x21\x2D' # measurement: periodic 1 mps, low repeatability
    CMD_MEAS_PERI_2_H   = b'\x22\x36' # measurement: periodic 2 mps, high repeatability
    CMD_MEAS_PERI_2_M   = b'\x22\x20' # measurement: periodic 2 mps, medium repeatability
    CMD_MEAS_PERI_2_L   = b'\x22\x2B' # measurement: periodic 2 mps, low repeatability
    CMD_MEAS_PERI_4_H   = b'\x23\x34' # measurement: periodic 4 mps, high repeatability
    CMD_MEAS_PERI_4_M   = b'\x23\x22' # measurement: periodic 4 mps, medium repeatability
    CMD_MEAS_PERI_4_L   = b'\x23\x29' # measurement: periodic 4 mps, low repeatability
    CMD_MEAS_PERI_10_H  = b'\x27\x37' # measurement: periodic 10 mps, high repeatability
    CMD_MEAS_PERI_10_M  = b'\x27\x21' # measurement: periodic 10 mps, medium repeatability
    CMD_MEAS_PERI_10_L  = b'\x27\x2A' # measurement: periodic 10 mps, low repeatability
    CMD_FETCH_DATA      = b'\xE0\x00' # readout measurements for periodic mode
    CMD_R_AL_LIM_LS     = b'\xE1\x02' # read alert limits, low set
    CMD_R_AL_LIM_LC     = b'\xE1\x09' # read alert limits, low clear
    CMD_R_AL_LIM_HS     = b'\xE1\x1F' # read alert limits, high set
    CMD_R_AL_LIM_HC     = b'\xE1\x14' # read alert limits, high clear
    CMD_W_AL_LIM_HS     = b'\x61\x1D' # write alert limits, high set
    CMD_W_AL_LIM_HC     = b'\x61\x16' # write alert limits, high clear
    CMD_W_AL_LIM_LC     = b'\x61\x0B' # write alert limits, low clear
    CMD_W_AL_LIM_LS     = b'\x61\x00' # write alert limits, low set
    CMD_NO_SLEEP        = b'\x30\x3E' # sleep

    # Repeatability
    REPEATAB_LOW = 4
    REPEATAB_MID = 6
    REPEATAB_HIGH = 15
    
    # Stop repeatability
    CMD_STOP_PERIODIC_MEASUREMENT = b'\x30\x93'
    
    # Frequencies
    FREQUENCY_HZ5 = 0.5
    FREQUENCY_1HZ = 1.0
    FREQUENCY_2HZ = 2.0
    FREQUENCY_4HZ = 4.0
    FREQUENCY_10HZ = 10.0

    I2C_ADDRESS = 0x45

    def __init__(self, sda_pin=Pin(21), scl_pin=Pin(22), i2cAddress=I2C_ADDRESS):
        self.i2c = I2C(1,sda=sda_pin, scl=scl_pin)
        self.i2c_address = i2cAddress
        
    # Check if address is found
    def isPresent(self):
        addresses = self.i2c.scan()
        return self.i2c_address in addresses
    
    
    # Calculate checksum with crc polynomial
    def _calcCrc(self, data):
        crc = 0xFF
        for b in data[0:2]:
            crc ^= b
            for a in range(8, 0, -1):
                if (crc & 0x80):
                    crc = (crc << 1) ^ SHT3X.POLYNOMIAL
                else:
                    crc <<= 1
        return crc;
    
    # Check crc after claculating it
    def _checkCrc(self, data):
        checksum = data[-1]
        crc = self._calcCrc(data)
        return checksum == crc
    
    # Sending commands to the sensor to receive a 6 bit return value
    def _sendCommand(self, command, response_size=6, delay=100):
        try:
            # Writing command to the sensor
            self.i2c.writeto(self.i2c_address, command)
        except OSError as exception:
            raise exception
        time.sleep_ms(delay)
        # Receiving data
        data = self.i2c.readfrom(self.i2c_address, response_size)
        # Dividing the data into two
        for i in range(response_size // 3):  # response_size // 3 = 2
            if self._checkCrc(data[i*3:(i+1)*3]):
                print ("CRC_ERROR")
            if data == bytearray(response_size): # If data is empty
                print ("DATA_ERROR")
        return data
    
    # Start periodic measurements
    def startPeriodicMeasurement(self, repeatability=False, frequency=0.5):
        # Setting repeatability if is not set
        if not repeatability:
            repeatability = self.REPEATAB_HIGH
        if (repeatability == self.REPEATAB_LOW):
            if (frequency == self.FREQUENCY_HZ5):
                value = self.i2c.writeto(self.i2c_address, self.CMD_MEAS_PERI_05_L)
            elif (frequency == self.FREQUENCY_1HZ):
                value = self.i2c.writeto(self.i2c_address, self.CMD_MEAS_PERI_1_L)
            elif (frequency == self.FREQUENCY_2HZ):
                value = self.i2c.writeto(self.i2c_address, self.CMD_MEAS_PERI_2_L)
            elif (frequency == self.FREQUENCY_4HZ):
                value = self.i2c.writeto(self.i2c_address, self.CMD_MEAS_PERI_4_L)
            elif (frequency == self.FREQUENCY_10HZ):
                value = self.i2c.writeto(self.i2c_address, self.CMD_MEAS_PERI_10_L)
            else:
                value = "PARAM ERROR"
        
        elif (repeatability == self.REPEATAB_MID):
            if (frequency == self.FREQUENCY_HZ5):
                value = self.i2c.writeto(self.i2c_address, self.CMD_MEAS_PERI_05_L)
            elif (frequency == self.FREQUENCY_1HZ):
                value = self.i2c.writeto(self.i2c_address, self.CMD_MEAS_PERI_1_L)
            elif (frequency == self.FREQUENCY_2HZ):
                value = self.i2c.writeto(self.i2c_address, self.CMD_MEAS_PERI_2_L)
            elif (frequency == self.FREQUENCY_4HZ):
                value = self.i2c.writeto(self.i2c_address, self.CMD_MEAS_PERI_4_L)
            elif (frequency == self.FREQUENCY_10HZ):
                value = self.i2c.writeto(self.i2c_address, self.CMD_MEAS_PERI_10_L)
            else:
                value = "PARAM ERROR"
                
        elif (repeatability == self.REPEATAB_HIGH):
            if (frequency == self.FREQUENCY_HZ5):
                value = self.i2c.writeto(self.i2c_address, self.CMD_MEAS_PERI_05_L)
            elif (frequency == self.FREQUENCY_1HZ):
                value = self.i2c.writeto(self.i2c_address, self.CMD_MEAS_PERI_1_L)
            elif (frequency == self.FREQUENCY_2HZ):
                value = self.i2c.writeto(self.i2c_address, self.CMD_MEAS_PERI_2_L)
            elif (frequency == self.FREQUENCY_4HZ):
                value = self.i2c.writeto(self.i2c_address, self.CMD_MEAS_PERI_4_L)
            elif (frequency == self.FREQUENCY_10HZ):
                value = self.i2c.writeto(self.i2c_address, self.CMD_MEAS_PERI_10_L)
            else:
                value = "PARAM ERROR"
        else:
            value = "PARAM ERROR"
        return value
    
    # Stop periodic measurement
    def stopPeriodicMeasurement(self):
        self._sendCommand(self.CMD_STOP_PERIODIC_MEASUREMENT)
        return
    
    # get measurement with clockstretching
    def _getTempAndHumiClkStretch(self, repeatability=False, timeout=100):
        if not repeatability:
            repeatability = self.REPEATAB_HIGH
            
        if (repeatability == self.REPEATAB_LOW):
             value = self._sendCommand(self.CMD_MEAS_CLOCKSTR_L)        
        elif (repeatability == self.REPEATAB_MID):
            value = self._sendCommand(self.CMD_MEAS_CLOCKSTR_M)                
        elif (repeatability == self.REPEATAB_HIGH):
            value = self._sendCommand(self.CMD_MEAS_CLOCKSTR_H)
        else:
            value = "PARAM ERROR"
        return value
    
    # get measurement with polling
    def _getTempAndHumiPolling(self, repeatability=False, timeout=100):
        if not repeatability:
            repeatability = self.REPEATAB_HIGH
            
        if (repeatability == self.REPEATAB_LOW):
             value = self._sendCommand(self.CMD_MEAS_POLLING_L)        
        elif (repeatability == self.REPEATAB_MID):
            value = self._sendCommand(self.CMD_MEAS_POLLING_M)                
        elif (repeatability == self.REPEATAB_HIGH):
            value = self._sendCommand(self.CMD_MEAS_POLLING_H)
        return value
            
    # Get temp and humid
    def getTempAndHumi(self, repeatability=False, polling=False, raw=False):
        if not polling:
            value = self._getTempAndHumiClkStretch(repeatability=repeatability)
            rawTemp = value[0] << 8 | value[1]
            rawHumi = value[3] << 8 | value[4]
            if raw:
                return rawTemp, rawHumi
            print (rawTemp)
            print (rawHumi)
            humi = self._calcHumi(rawHumi)
            temp = self._calcTemp(rawTemp)
        else:
            value = self._getTempAndHumiPolling(repeatability=repeatability)
            rawTemp = value[0] << 8 | value[1]
            rawHumi = value[3] << 8 | value[4]
            if raw:
                return rawTemp, rawHumi
            print (rawTemp)
            print (rawHumi)
            humi = self._calcHumi(rawHumi)
            temp = self._calcTemp(rawTemp)
        return temp, humi
    
    # Read measurement buffer
    # Does not work
    #def readMeasurementBuffer(self):
     #   value = self._sendCommand(self.CMD_FETCH_DATA)
    #    return value[0]
            
    # Calc temp
    def _calcTemp(self, rawTemp):
        return -45.0 + 175.0 * rawTemp / 65536.0
    
    # Calc humid
    def _calcHumi(self, rawHumi):
        return 100.0 * rawHumi / 65536.0
    
    def calcRawTemp(self, temp):
        return (temp + 45.0) / 175.0 * 65535.0
    
    def calcRawHumi(self, humi):
        return humi / 100.0 * 65535.0
    
    def celcToFarh(self, celc):
        return (celc * (9/5)) + 32
    
    def farhToCelc(self, farh):
        return (farh - 32) * 5/9
    
    # Soft reset
    # Tells me OSError: [Errno 19] ENODEV
    #def softReset(self):
     #   return self._sendCommand(self.CMD_SOFT_RESET)
    
    def readStatus(self):
        status = self._sendCommand(self.CMD_READ_STATUS)
        return status
    
    def clearAllAlerts(self):
        return self._sendCommand(self.CMD_CLEAR_STATUS)
    
    def enableHeater(self):
        return self._sendCommand(self.CMD_HEATER_ENABLE)
    
    def disableHeater(self):
        return self._sendCommand(self.CMD_HEATER_DISABLE)


    

    