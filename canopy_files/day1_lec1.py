# coding: utf-8
from numpy import *
from matplotlib import *
import sys
from pylab import *
pi = 3.14
x = linspace(-5 * pi, 5 * pi, 500)
plot(sin(x), 'r')
plot(x * sin(x), 'r')
plot(x, 'g')
plot(-x, 'g')
legend(['sin(2y)', 'cos(y)', 'x', '-x'])
