#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 15:46:31 2019
@author: david
"""

import numpy as np
import matplotlib.pyplot as plt
from physique.modelisation import ajustement_affine

x=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y =[2.2, 4.1, 5.9, 8.2, 9.8, 11.9, 13.1, 16, 18.1, 19.8]

a, b = ajustement_affine(x, y, plot_axes=plt, plot_xmax=10)
print(a, b)

#x_mod = np.linspace(0,max(x),50)
#y_mod = a*x_mod

#plt.plot(x_mod, y_mod, '-')

plt.plot(x, y, '+r', label="Mesures")
plt.legend()
plt.xlim(0, 10)
plt.ylim(0, 30)
plt.grid()
plt.show()
