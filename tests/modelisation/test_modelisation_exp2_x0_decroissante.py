#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 15:46:31 2019
@author: david
Ne fonctionne pas bien pour x0 car une infinité de solution en fonction de A
"""

import numpy as np
import matplotlib.pyplot as plt
from physique import exponentielleDecroissante, ajustementExponentielleDecroissanteX0

x=np.array([2,3,4,5,6,7,8,9,10,11])
y=np.array([4.98, 3.59, 2.57, 1.83, 1.32, 0.93, 0.67, 0.48, 0.34, 0.25])

# Modélisation
A, tau, x0 = ajustementExponentielleDecroissanteX0(x, y, x0_p0=2)
print(A, tau, x0)

# Tracé du modèle
x_mod = np.linspace(0,20,50)
y_mod = exponentielleDecroissante(x_mod,A,tau,x0)


plt.plot(x_mod, y_mod, '-')
#plt.plot(x_mod, y_reel, 'r-')
plt.plot(x, y, 'x')
plt.grid()
plt.show()
