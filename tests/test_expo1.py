#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 15:46:31 2019

@author: david
"""

import numpy as np
import matplotlib.pyplot as plt
from physique import exp1, ajustement_exp1

plt.rcParams['figure.dpi'] = 100

#x=np.array([0,1,2,3,4,5,6,7,8,9])
#y=np.array([0.,3.935,6.321,7.769,8.647,9.179,9.502,9.698,9.817,9.889])

x=[0,1,2,3,4,5,6,7,8,9]
y=[0.,3.935,6.321,7.769,8.647,9.179,9.502,9.698,9.817,9.889]

A, tau, x0 = ajustement_exp1(x,y)    
    
print("A= ",A)
print("tau=",tau)

xnew = np.linspace(0,10,50)
ynew = exp1(xnew,A,tau)   # use interpolation function returned by `interp1d`

plt.plot(xnew, ynew, '-')
plt.plot(x, y, 'x')
plt.show()