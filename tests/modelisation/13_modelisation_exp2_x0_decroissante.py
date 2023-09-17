#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 15:46:31 2019
@author: david
Ne fonctionne pas bien pour x0 car une infinité de solution en fonction de A
"""

import numpy as np
import matplotlib.pyplot as plt
from physique.modelisation import ajustement_exponentielle_decroissante_x0

x=np.array([2,3,4,5,6,7,8,9,10,11])
y=np.array([4.98, 3.59, 2.57, 1.83, 1.32, 0.93, 0.67, 0.48, 0.34, 0.25])

# Modélisation
A, tau, x0, line1 = ajustement_exponentielle_decroissante_x0(x, y, plot_ax=plt, plot_xmax=20, return_line=True)
line1.set(linestyle="--")
print(A, tau, x0)


plt.plot(x, y, '+', label="Mesures")
plt.legend()
plt.xlim(0,20)
plt.grid()
plt.show()
