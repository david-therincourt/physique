#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 15:46:31 2019
@author: david
"""

import numpy as np
import matplotlib.pyplot as plt
from physique import exponentielleCroissante, ajustementExponentielleCroissante

x=np.array([0,1,2,3,4,5,6,7,8,9])
y=np.array([0.,3.935,6.321,7.769,8.647,9.179,9.502,9.698,9.817,9.889])

# Modélisation
A, tau = ajustementExponentielleCroissante(x, y)
print(A, tau)

# Tracé du modéle
x_mod = np.linspace(0,10,50)
y_mod = exponentielleCroissante(x_mod,A,tau)

plt.plot(x_mod, y_mod, '-')
plt.plot(x, y, 'x')
plt.grid()
plt.show()
