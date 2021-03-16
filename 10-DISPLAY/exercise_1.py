from ST7735 import Display
import fonts.sysfont as sysfont
from machine import SPI,Pin
import time
import math
import sys
import random

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


def randomLines(color, number=None):
    print("Random lines")
    tft.clear()
    if number == None:
        number = 50
    for _ in range(number):
        x_start = random.randint(0, 127)
        x_end = random.randint(0, 127)
        y_start = random.randint(0, 127)
        y_end = random.randint(0, 127)
        tft.draw_line(x_start, y_start, x_end, y_end, color)
    time.sleep(5)
    tft.clear()

def randomRectangles(color, number=None):
    print("Random rectangles")
    tft.clear()
    if number == None:
        number = 50
    for _ in range(number):
        x_start = random.randint(0, 127)
        width = random.randint(0, 127)
        y_start = random.randint(0, 127)
        height = random.randint(0, 127)
        tft.draw_rectangle(x_start, y_start, width, height, color)
    time.sleep(5)
    tft.clear()
    
def randomCirlces(color, number=None):
    print("Random circles")
    tft.clear()
    if number == None:
        number = 50
    for _ in range(number):
        x_start = random.randint(0, 127)
        y_start = random.randint(0, 127)
        radius = random.randint(0, 63)
        tft.draw_circle(x_start, y_start, radius, color)
    time.sleep(5)
    tft.clear()
    
def rand():
    randomLines(Display.RED)
    randomRectangles(Display.BLUE)
    randomCirlces(Display.YELLOW)
    

# print(tft.size())
rand()