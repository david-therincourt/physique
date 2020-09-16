#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 15:46:31 2019
@author: david
"""

import numpy as np
import matplotlib.pyplot as plt
from physique import ajustement_lineaire

x=[0,1,2,3,4,5,6,7,8,9]
y =[0.2,2.1,3.9,6.2,7.8,9.9,12.1,14,16.1,17.8]

a = ajustement_lineaire(x, y)
print(a)

x_mod = np.linspace(0,max(x),50)
y_mod = a*x_mod

plt.plot(x_mod, y_mod, '-')
plt.plot(x, y, 'x')
plt.grid()
plt.show()
