height = 128 # 1.5 inch 128*128 display

from machine import Pin,SPI
import gc,sys
from ST7735 import Display,color565
import fonts.sysfont as sysfont
import cmath
import utime
import uos
from writer import Writer, CWriter
from nanogui import Label, Meter, LED, Dial, Pointer, refresh

if sys.platform == 'esp32':
    print('1.4 inch TFT screen test on ESP32')
    sck = Pin(18)
    miso= Pin(19)
    mosi= Pin(23)
    SPI_CS = 26
    SPI_DC = 5
    spi = SPI(2, baudrate=32000000, sck=sck, mosi=mosi, miso=miso)

tft =Display(spi,SPI_CS,SPI_DC)    
# Fonts
import fonts.arial10 as arial10
import fonts.freesans20 as freesans20

GREEN = color565(0, 255, 0)
RED = color565(255, 0, 0)
BLUE = color565(0, 0, 255)
YELLOW = color565(255, 255, 0)
BLACK = 0
CWriter.set_textpos(tft, 0, 0)  # In case previous tests have altered it
wri = CWriter(tft, arial10, GREEN, BLACK, verbose=False)
wri.set_clip(True, True, False)
        
        
class Point():
    def __init__(self, dial):
        self.dial = dial
        self.val = 0 + 0j
        self.color = None

    def value(self, v=None, color=None):
        self.color = color
        if v is not None:
            if isinstance(v, complex):
                l = cmath.polar(v)[0]
                if l > 1:
                    self.val = v/l
                else:
                    self.val = v
            else:
                raise ValueError('Pointer value must be complex.')
#         self.dial.vectors.add(self)
        self.dial._set_pend(self.dial)  # avoid redrawing for each vector
        return self.val
        
def _set_pend(cls, obj):
    cls.devices[obj.device].add(obj)


def circ(color, number=None):
    tft.clear()
    if number == None:
        number = 50
#     for _ in range(number):
    x0 = 63
    y0 = 80
    r = 60
    f = 1 - r
    dx = 1
    dy = -r - r
    x = 0
    y = r
#     tft.draw_pixel(x0, y0 + r, color)
    tft.draw_pixel(x0, y0 - r, color)
    tft.draw_pixel(x0 + r, y0, color)
    tft.draw_pixel(x0 - r, y0, color)
    while x < y:
        if f >= 0:
            y -= 1
            dy += 2
            f += dy
        x += 1
        dx += 2
        f += dx
        tft.draw_pixel(x0 + x, y0 - y, color)
        tft.draw_pixel(x0 - x, y0 - y, color)
        tft.draw_pixel(x0 + y, y0 - x, color)
        tft.draw_pixel(x0 - y, y0 - x, color)
        
#   Calibrations
#     tft.draw_line(105, 37, 100, 42, Display.YELLOW)
#     tft.draw_line(12, 48, x0, y0, Display.YELLOW)
    tft.draw_line(85, 24, 82, 32, Display.GREEN)
    tft.draw_line(41, 24, 44, 32, Display.GREEN)
    tft.draw_line(114, 48, 106, 53, Display.GREEN)
    tft.draw_line(12, 48, 18, 53, Display.GREEN)
    

#   Bottom line
    for a in range(1, 2*r):
        tft.draw_pixel((x0 + r) - a, y0, color)
        
    tft.draw_text((x0//2)+2,y0-(r+15),"VOLTMETER", sysfont, Display.WHITE)
    tft.draw_text((x0-r),y0+5,"0.0V", sysfont, Display.GREEN)
    tft.draw_text((x0+r)-25,y0+5,"5.0V", sysfont, Display.GREEN)
    
    tft.draw_text(0,y0+25,"voltage:", arial10, Display.GREEN)
    reading = str(1.0)
    tft.draw_text(50,y0+25,"1.0V", arial10, Display.GREEN)
    
#     Pointer or meter
#     tft.draw_line(x0, y0, x0-r+10, y0, Display.RED)
#     tft.draw_line(x0-r+10, y0, x0-r+17, y0-5, Display.RED)
#     
    tft.draw_line(x0, y0, 20, 55, Display.RED)
    tft.draw_line(20, 55, 22, 61, Display.RED)
    tft.draw_line(20, 55, 26, 54, Display.RED)
    
    shift = cmath.polar(0 + 1j)
#     
#     tft.draw_line(x0, y0, 45, 35, Display.RED)
#     tft.draw_line(45, 35, 42, 40, Display.RED)
#     tft.draw_line(45, 35, 51, 37, Display.RED)
#     
#     tft.draw_line(x0, y0, 80, 35, Display.RED)
#     tft.draw_line(80, 35, 75, 37, Display.RED)
#     tft.draw_line(80, 35, 83, 40, Display.RED)
#     
#     tft.draw_line(x0, y0, 103, 54, Display.RED)
#     tft.draw_line(103, 54, 97, 54, Display.RED)
#     tft.draw_line(103, 54, 101, 60, Display.RED)
#     
#     tft.draw_line(x0, y0, x0+r-10, y0, Display.RED)
#     tft.draw_line(x0+r-10, y0, x0+r-17, y0-5, Display.RED)
    
    



dial = circ(Display.GREEN)

# bearing = Point(dial)
# bearing.value(0 + 1j, RED)
# dh = cmath.rect(1, -cmath.pi/30)  # Rotate by 6 degrees CW
# for n in range(7):
#     utime.sleep_ms(200)
#     bearing.value(bearing.value() * dh, RED)
#     refresh(tft)
    
while True: 
    print(cmath.exp(2j * cmath.pi/10))

