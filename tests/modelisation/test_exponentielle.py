#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 15:46:31 2019
@author: david
"""

import numpy as np
import matplotlib.pyplot as plt
from physique.modelisation import *



# Exponentielle
#x = [0,1,2,3,4,5,6,7,8,9]
#y = [0.,3.935,6.321,7.769,8.647,9.179,9.502,9.698,9.817,9.889]

# Exponentielle x0 
#x = [2,3,4,5,6,7,8,9,10,11]
#y = [0.,3.935,6.321,7.769,8.647,9.179,9.502,9.698,9.817,9.889]

# Exponentielle decroissante
x = [0,1,2,3,4,5,6,7,8,9]
y = [4.98, 3.59, 2.57, 1.83, 1.32, 0.93, 0.67, 0.48, 0.34, 0.25]

# Exponentielle decroissante x0
#x = [2,3,4,5,6,7,8,9,10,11]
#y = [4.98, 3.59, 2.57, 1.83, 1.32, 0.93, 0.67, 0.48, 0.34, 0.25]

modele = ajustement_exponentielle2_decroissante(x,y)
print(modele.values())
print(modele.text())
print(modele.pcov())

plt.plot(x, y, '+r', label="Mesures")
modele.plot()
plt.legend()
plt.grid()
plt.show()
