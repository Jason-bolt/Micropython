import matplotlib.pyplot as pl
import numpy as np


x, y = np.loadtxt('adc_external.txt', delimiter=',', unpack=True)
pl.plot(x,y)
pl.show()

#print(np.polyfit(x, y, 10))

