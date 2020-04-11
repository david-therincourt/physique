# -*- coding: utf-8 -*-
"""
Test de pilotage d'une PyBoard en mode REPL
exec(open("tests/micropython/test_pilotage.py").read())
"""
import matplotlib.pyplot as plt
import numpy as np
from physique.micropython import execFichier

# Exécution du programme et récupération des données par le port série
data = execFichier("tests/micropython/condensateur.py", "/dev/ttyACM0") # Exécution du programme sur la PyBoard
x,y = eval(data)    # Conversion des données sous forme d'un chaine de caractères en un tuple (x, y)

t = np.array(x)
u = np.array(y)

plt.plot(t,u,'r.')
plt.title("R = 100 k et C = 330 nF")
plt.xlabel("t(ms)")
plt.ylabel("uc")
plt.grid()
plt.xlim(-t.max()/5,t.max())
plt.ylim(0,5000)
plt.show()
