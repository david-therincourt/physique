# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 23:27:11 2020
exec(open("tests/csv/test_import_regavi.py").read())
@author: david
"""

import numpy as np
import matplotlib.pyplot as plt
from physique.csv import importRegavi

t, x, y = importRegavi('tests/csv/data_regavi.txt')

plt.plot(x,y,'.')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.grid()
plt.title("Trajectoire d 'un ballon")
plt.show()
