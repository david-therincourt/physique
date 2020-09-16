#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 15:46:31 2019
@author: david
"""

import numpy as np
import matplotlib.pyplot as plt
from physique import exponentielle_decroissante, ajustement_exponentielle_decroissante

x=np.array([0,1,2,3,4,5,6,7,8,9])
y=np.array([4.98, 3.59, 2.57, 1.83, 1.32, 0.93, 0.67, 0.48, 0.34, 0.25])

# Modélisation
A, tau = ajustement_exponentielle_decroissante(x, y)
print(A, tau)

# Tracé du modèle
x_mod = np.linspace(0,20,50)
y_mod = exponentielle_decroissante(x_mod,A,tau)

plt.plot(x_mod, y_mod, '-')
plt.plot(x, y, 'x')
plt.grid()
plt.show()
