height = 128 # 1.5 inch 128*128 display

from machine import Pin,SPI
import gc,sys
from ST7735 import Display,color565
import cmath
import utime
import uos
from writer import Writer, CWriter
from nanogui import Label, Meter, LED, Dial, Pointer, refresh
# SHT30 IMPORT
from sht3x import SHT3X

if sys.platform == 'esp32':
    print('1.4 inch TFT screen test on ESP32')
    sck = Pin(18)
    miso= Pin(19)
    mosi= Pin(23)
    SPI_CS = 26
    SPI_DC = 5
    spi = SPI(2, baudrate=32000000, sck=sck, mosi=mosi, miso=miso)

st7735 =Display(spi,SPI_CS,SPI_DC)    
# Fonts
import fonts.arial10 as arial10
import fonts.freesans20 as freesans20

GREEN = color565(0, 255, 0)
RED = color565(255, 0, 0)
BLUE = color565(0, 0, 255)
YELLOW = color565(255, 255, 0)
BLACK = 0
CWriter.set_textpos(st7735, 0, 0)  # In case previous tests have altered it
wri = CWriter(st7735, arial10, GREEN, BLACK, verbose=False)
wri.set_clip(True, True, False)

def meter():
    
    print('Meter test.')
    refresh(st7735, True)  # Clear any prior image
#     FOR TEMPERATURE
    color_temp = lambda v : RED if v > 40 else YELLOW if v > 27 else GREEN
    m0 = Meter(wri, 5, 12, height=60, divisions = 5, ptcolor=BLUE,
              label='temp', style=Meter.BAR, legends=('0', '10', '20', '30', '40', '50'))
    l0 = LED(wri, st7735.height - 46 - wri.height, 12, bdcolor=YELLOW, label ='0')

#     FOR HUMIDITY
#     color_humid = lambda v : RED if v > 0.8 else YELLOW if v > 0.6 else GREEN
    m1 = Meter(wri, 5, 80, height=60, divisions = 5, ptcolor=YELLOW,
              label='right', style=Meter.BAR, legends=('0', '20', '40', '60', '80', '100'))
    l1 = LED(wri, st7735.height - 46 - wri.height, 80, bdcolor=YELLOW, label ='0')

    sensor = SHT3X()
    # print(sensor.isPresent())
    
    while True:
        temp, humid = sensor.getTempAndHumi()
        print("Temporature:", temp, 'ºC, RH:', humid, '%')

        l0.text(str(temp)[:4])
        l1.text(str(humid)[:4])

        mtemp = temp / 50
        mhumid = humid / 100
        m0.value(mtemp, color_temp(temp))
        m1.value(mhumid)

        refresh(st7735)
        utime.sleep(1)



# print('Color display test is running.')
meter()

# print('Test complete.')
