#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 15:46:31 2019
exec(open("tests/modelisation/test_modelisation_exp1_x0_croissante.py").read())
@author: david
"""

import numpy as np
import matplotlib.pyplot as plt
from physique.modelisation import exp1, ajustement_exp1_x0

x=np.array([2,3,4,5,6,7,8,9,10,11])
y=np.array([0.,3.935,6.321,7.769,8.647,9.179,9.502,9.698,9.817,9.889])

# Modélisation
A, tau, x0 = ajustement_exp1_x0(x, y)
print(A, tau, x0)

# Tracé du modéle
x_mod = np.linspace(0,20,50)
y_mod = exp1(x_mod,A,tau,x0)

plt.plot(x_mod, y_mod, '-')
plt.plot(x, y, 'x')
plt.grid()
plt.show()
