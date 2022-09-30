#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 15:46:31 2019
@author: david
"""

import numpy as np
import matplotlib.pyplot as plt
from physique import ajustement_lineaire
from mplcursors import Cursor

x = [1.0, 2.0, 3.0, 4.0, 5.0,  6.0,  7.0,  8.0,  9.0]
y = [2.1, 3.9, 6.2, 7.8, 9.9, 12.1, 14.0, 16.1, 17.8]

a, axes1 = ajustement_lineaire(x, y, plot_xmin=0, plot_ax=plt, return_line=True)
axes1.set(color="C2", linestyle="--")
Cursor([axes1])

print(a)



plt.plot(x, y, '+', label="Mesures")
plt.legend()
plt.xlim(0,10)
plt.ylim(0,20)
plt.grid()
plt.show()
