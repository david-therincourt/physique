#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 15:46:31 2019
@author: david
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from fonctions import *

def somme_sqrt(cov):
    diag = np.diag(pcov)
    s = 0
    for val in diag:
        s = s + val**2
    return s

# Affine
#x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#y = [2.2, 4.1, 5.9, 8.2, 9.8, 11.9, 13.1, 16, 18.1, 19.8]

# Exponentielle
#x = [0,1,2,3,4,5,6,7,8,9]
#y = [0.,3.935,6.321,7.769,8.647,9.179,9.502,9.698,9.817,9.889]

# Exponentielle x0 
x = [1,2,3,4,5,6,7,8,9,10]
y = [0.,4,6,8,8.647,9.179,9.502,9.698,9.817,9.889]

# Exponentielle decroissante
#x = [0,1,2,3,4,5,6,7,8,9]
#y = [4.98, 3.59, 2.57, 1.83, 1.32, 0.93, 0.67, 0.48, 0.34, 0.25]

# Exponentielle decroissante x0
#x = [2,3,4,5,6,7,8,9,10,11]
#y = [4.98, 3.59, 2.57, 1.83, 1.32, 0.93, 0.67, 0.48, 0.34, 0.25]

(A,tau), pcov  = curve_fit(exponentielle_croissante, x, y, p0=[1,1])
print(somme_sqrt(pcov))

(A,tau,x0), pcov  = curve_fit(exponentielle_croissante_x0, x, y, p0=[1,1,0])
print(somme_sqrt(pcov))

(A,tau), pcov  = curve_fit(exponentielle_decroissante, x, y, p0=[1,1])
print(somme_sqrt(pcov))


xmod = np.linspace(0,11,100)
ymod = A*np.exp(-xmod/tau)

plt.plot(x,y, "+")
plt.plot(xmod,ymod)
plt.show()

