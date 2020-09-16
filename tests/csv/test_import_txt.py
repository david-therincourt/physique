# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 23:27:11 2020
@author: david
"""

#import numpy as np
import matplotlib.pyplot as plt
from physique.csv import import_txt

x, y = import_txt('data.txt')

plt.plot(x,y,'.')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.grid()
plt.show()
