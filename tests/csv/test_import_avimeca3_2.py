# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 23:27:11 2020
exec(open("tests/csv/test_import_avimeca3_2.py").read())
@author: david
"""

import numpy as np
import matplotlib.pyplot as plt
from physique.csv import importAvimeca3

t, x, y = importAvimeca3('tests/csv/data2_avimeca3.txt', sep = ';')

plt.plot(x,y,'.')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.grid()
plt.title("Trajectoire d 'un ballon")
plt.show()
