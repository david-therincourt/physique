#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 15:46:31 2019
@author: david
"""

import numpy as np
import matplotlib.pyplot as plt
from physique.modelisation import ajustement_parabolique
from mplcursors import cursor

x = np.array([0.003,0.141,0.275,0.410,0.554,0.686,0.820,0.958,1.089,1.227,1.359,1.490,1.599,1.705,1.801])
y = np.array([0.746,0.990,1.175,1.336,1.432,1.505,1.528,1.505,1.454,1.355,1.207,1.018,0.797,0.544,0.266])

a, b, c, line1 = ajustement_parabolique(x, y, plot_ax=plt, plot_xmin=-0.2, plot_xmax=2, return_line=True)
print(a, b, c)
cursor([line1])


plt.plot(x, y, '+', label="Mesures")
plt.legend()
plt.grid()
plt.show()
