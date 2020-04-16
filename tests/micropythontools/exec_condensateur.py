# -*- coding: utf-8 -*-
"""
Test de pilotage d'une PyBoard en mode REPL

"""
import matplotlib.pyplot as plt
import numpy as np
from physique.micropythontools import execFileOnBoard

# Exécution du programme et récupération des données par le port série
x, y = execFileOnBoard("condensateur.py", "/dev/ttyACM0") # Exécution du programme sur la PyBoard

t = np.array(x)
u = np.array(y)

plt.plot(t,u,'r.')
plt.title("R = 100 k et C = 220 nF")
plt.xlabel("t(ms)")
plt.ylabel("uc")
plt.grid()
plt.xlim(-t.max()/5,t.max())
plt.ylim(0,5000)
plt.show()
