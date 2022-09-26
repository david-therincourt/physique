#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 15:46:31 2019
@author: david
"""

import numpy as np
import matplotlib.pyplot as plt
from physique.modelisation import *

x=np.array([0,1,2,3,4,5,6,7,8,9])
y=np.array([0.,3.935,6.321,7.769,8.647,9.179,9.502,9.698,9.817,9.889])

# Modélisation
A, tau = ajustement_exponentielle_croissante(x, y, plot_axes=plt)
print(A, tau)


plt.plot(x, y, 'x', label="Mesures")
plt.legend()
plt.grid()
plt.show()
