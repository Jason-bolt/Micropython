height = 128 # 1.5 inch 128*128 display

from machine import Pin,SPI
import gc,sys
from ST7735 import Display, color565

# Initialise hardware and framebuf before importing modules
# Initialise hardware
if sys.platform == 'esp32':
    print('1.4 inch TFT screen test on ESP32')
    sck = Pin(18)
    miso= Pin(19)
    mosi= Pin(23)
    SPI_CS = 26
    SPI_DC = 5
    spi = SPI(2, baudrate=32000000, sck=sck, mosi=mosi, miso=miso)
    
st7735=Display(spi,SPI_CS,SPI_DC)

import cmath
import math
import utime
import uos
from writer import Writer, CWriter
from fplot import PolarGraph, PolarCurve, CartesianGraph, Curve, TSequence
from nanogui import Label, refresh

refresh(st7735)

# Fonts
import fonts.arial10 as arial10
import fonts.freesans20 as freesans20

GREEN = color565(0, 255, 0)
RED = color565(255, 0, 0)
BLUE = color565(0, 0, 255)
YELLOW = color565(255, 255, 0)
WHITE = color565(255, 255, 255)
BLACK = 0
LIGHTGREEN = color565(0, 100, 0)

CWriter.set_textpos(st7735, 0, 0)  # In case previous tests have altered it
wri = CWriter(st7735, arial10, GREEN, BLACK, verbose=False)
wri.set_clip(True, True, False)


def seq():
    print('Time sequence test - sine and cosine.')
    refresh(st7735, True)  # Clear any prior image
    # y axis at t==now, no border
    g = CartesianGraph(wri, 32, 2, height=80, xorigin = 10, fgcolor=False,
                       gridcolor=LIGHTGREEN, bdcolor=WHITE)
#     tsy = TSequence(g, YELLOW, 50)
#     tsr = TSequence(g, RED, 50)
    lbl = Label(wri, 10, 5, 'label')
    lbl.value("DAMPED OSCILLATOR")
    plt = TSequence(g, WHITE, 200)
    r = 0.9
    p = 0
    for t in range(300):
        g.clear()
#         tsy.add(0.9*math.sin(t/10))
#         tsr.add(0.4*math.cos(t/10))
        plt.add(r*math.cos(t/10))
        r = r - 0.003
        refresh(st7735)
#         print(r)
        utime.sleep_ms(1)
        p = p + 1
#         print(p)
#         print(t)

gc.collect()  # Precaution before instantiating framebuf
seq()
