"""
Test de pilotage d'une PyBoard en mode REPL

"""
import matplotlib.pyplot as plt
from physique.micropythontools import execFileOnBoard

# Exécution du programme et récupération des données par le port série
x, y = execFileOnBoard("read_adc.py", "/dev/ttyACM0") # Exécution du programme sur la PyBoard

plt.plot(x,y,'r.')
plt.ylim(0,5000)
plt.show()
