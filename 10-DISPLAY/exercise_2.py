from ST7735 import Display
import fonts.sysfont as sysfont
from machine import SPI,Pin
import time
import math
import sys
import fonts.ArcadePix9x11 as ArcadePix9x11
import fonts.Bally7x9 as Bally7x9
import fonts.Broadway17x15 as Broadway17x15
import fonts.EspressoDolce18x24 as EspressoDolce18x24
import fonts.FixedFont5x8 as FixedFont5x8
import fonts.Neato5x7 as Neato5x7
import fonts.Robotron7x11 as Robotron7x11
import fonts.Unispace12x24 as Unispace12x24
import fonts.Wendy7x8 as Wendy7x8


if sys.platform == 'esp32':
    print('1.4 inch TFT screen test on ESP32')
    sck = Pin(18)
    miso= Pin(19)
    mosi= Pin(23)
    SPI_CS = 26
    SPI_DC = 5
    spi = SPI(2, baudrate=32000000, sck=sck, mosi=mosi, miso=miso)
#     tft=Display(spi,SPI_DC,SPI_CS)
    tft=Display(spi,SPI_CS,SPI_DC)

def text():
    print("Write DCSIT")
    tft.clear()
    tft.draw_text(0,0,"DSCIT", ArcadePix9x11, Display.GREEN)
    tft.draw_text(0,12,"DSCIT", Bally7x9, Display.RED)
    tft.draw_text(0,24,"DSCIT", Broadway17x15, Display.PINK)
    tft.draw_text(0,40,"DSCIT", EspressoDolce18x24, Display.YELLOW)
    tft.draw_text(0,63,"DSCIT", FixedFont5x8, Display.BLUE)
    tft.draw_text(0,74,"DSCIT", Neato5x7, Display.ORANGE)
    tft.draw_text(0,84,"DSCIT", Robotron7x11, Display.ORANGE)
    tft.draw_text(0,98,"DSCIT", Unispace12x24, Display.ORANGE)
    tft.draw_text(80,100,"DSCIT", Wendy7x8, Display.ORANGE, landscape=True)
    

text()