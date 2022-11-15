# float to int and round to up
import math
print(math.ceil(2/10))
# 1
# Exceptios
def double(x):
    if type(double)!= type(1):
      raise Exception("x must be an integer!")
double("10")
#?
#==================================================
# Time
## Seconds to hhh:mm:ss
from datetime import timedelta

sec = 6010
print('Time in Seconds:', sec)

td = timedelta(seconds=sec)
print('Time in hh:mm:ss:', td)
#??
# https://pynative.com/python-convert-seconds-to-hhmmss/
#-------------------------------
# Numpy
# Get histogram of the sequency
import numpy as np
numbers = [2,1,2,3,2,10,1]
hist = np.histogram(numbers,bins=range(10))
print(hist[0])
# ??
print(hist[1])
# ??
numbers_2 = [10,5,1.2,1.3,1.9,2,2.9]
hist = np.histogram(numbers_2,bins=[0,2])
print(hist[0])
# ??
print(hist[1])
# ??
