from ST7735 import Display
import fonts.sysfont as sysfont
from machine import SPI,Pin
import time
import math
import sys

if sys.platform == 'esp32':
    print('1.4 inch TFT screen test on ESP32')
    sck = Pin(18)
    miso= Pin(19)
    mosi= Pin(23)
    SPI_CS = 26
    SPI_DC = 5
    spi = SPI(2, baudrate=32000000, sck=sck, mosi=mosi, miso=miso)
    tft=Display(spi,SPI_DC,SPI_CS)
    
tft=Display(spi,SPI_CS,SPI_DC)    
    
def players():
    tft.clear()
    print("Setting up the players!")
#   ***** player 1 *****
    tft.draw_text(0, 0, "Player1: ", sysfont, Display.GREEN)
    tft.draw_text(50, 0, "1", sysfont, Display.GREEN)
#     winner
    tft.draw_text(75, 0, "Winner", sysfont, Display.GREEN)
    
#   bottom line
    tft.draw_hline(0, 11, tft.size()[0], Display.WHITE)

#   ***** player 2 *****
    tft.draw_text(0, 14, "Player2: ", sysfont, Display.YELLOW)
    tft.draw_text(50, 14, "1", sysfont, Display.YELLOW)
#     winner
    tft.draw_text(75, 14, "Winner", sysfont, Display.YELLOW)
    
#   bottom line
    tft.draw_hline(0, 25, tft.size()[0], Display.WHITE)

#   ***** player 3 *****
    tft.draw_text(0, 28, "Player3: ", sysfont, Display.RED)
    tft.draw_text(50, 28, "1", sysfont, Display.RED)
#     winner
    tft.draw_text(75, 28, "Winner", sysfont, Display.RED)
    
#   bottom line
    tft.draw_hline(0, 39, tft.size()[0], Display.WHITE)

#   ***** player 4 *****
    tft.draw_text(0, 44, "Player4: ", sysfont, Display.ORANGE)
    tft.draw_text(50, 44, "1", sysfont, Display.ORANGE)
#     winner
    tft.draw_text(75, 44, "Winner", sysfont, Display.ORANGE)
    
#   bottom line
    tft.draw_hline(0, 55, tft.size()[0], Display.WHITE)
#     tft.clear()
#     tft.draw_text(0,127, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur adipiscing ante sed nibh tincidunt feugiat. Maecenas enim massa, fringilla sed malesuada et, malesuada sit amet turpis. Sed porttitor neque ut ante pretium vitae malesuada nunc bibendum. Nullam aliquet ultrices massa eu hendrerit. Ut sed nisi lorem. In vestibulum purus a tortor imperdiet posuere. ", sysfont, Display.WHITE,landscape=True)
#     time.sleep(5)



players()