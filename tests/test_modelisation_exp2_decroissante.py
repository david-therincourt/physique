#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 15:46:31 2019

@author: david
"""

import numpy as np
import matplotlib.pyplot as plt
from physique import exp2, ajustement_exp2

x=np.array([0,1,2,3,4,5,6,7,8,9])
y=np.array([4.98, 3.59, 2.57, 1.83, 1.32, 0.93, 0.67, 0.48, 0.34, 0.25])

A, tau, x0 = ajustement_exp2(x, y, 4.8 ,2.9 , 0) # Difficile à converger !!!

print("A= ",A)
print("tau=",tau)

x_mod = np.linspace(0,10,50)
y_mod = exp2(x_mod,A,tau)

plt.plot(x_mod, y_mod, '-')
plt.plot(x, y, 'x')
plt.show()