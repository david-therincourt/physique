#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 15:46:31 2019
@author: david
"""

from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
from physique.modelisation import *

x=np.array([2,3,4,5,6,7,8,9,10,11])
y=np.array([0.,3.935,6.321,7.769,8.647,9.179,9.502,9.698,9.817,9.889])

# Modélisation
A, tau, x0, line1 = ajustement_exponentielle_croissante_x0(x, y, plot_ax=plt, return_line=True)
line1.set(color = "C2")
print(A, tau, x0)



plt.plot(x, y, '+', label="Mesures")
plt.legend()
plt.xlim(0,11)
plt.grid()
plt.show()
