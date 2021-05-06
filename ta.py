import numpy
import talib
from numpy import genfromtxt

my_data = genfromtxt('15minutes.csv', delimiter=',')

close = my_data[:, 4]

rsi = talib.RSI(close)

print(rsi)