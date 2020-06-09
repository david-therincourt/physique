# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 23:27:11 2020
@author: david
"""

import numpy as np
import matplotlib.pyplot as plt
from physique.csv import importAvimeca3Txt

t, x, y = importAvimeca3Txt('data2_avimeca3.txt', sep = ';')

plt.plot(x,y,'.')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.grid()
plt.title("Trajectoire d 'un ballon")
plt.show()
