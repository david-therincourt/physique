import numpy as np
import matplotlib.pyplot as plt
from physique.modelisation import ajustement_gain_ordre2_passe_bande

### IMPORTATION ###
f, Us = np.loadtxt('wien.csv', delimiter=',', skiprows=1, unpack=True)

### CACLCULS ###
Ue = 4.44
G = 20*np.log10(Us/Ue)


### MODELISATION ###
G0, f0, m = ajustement_gain_ordre2_passe_bande(f, G, plot_ax=plt)
print("G0 = {} \t f0 = {} \t m = {}".format(G0, f0, m))


### COURBE ###
plt.plot(f, G, '+', label='Mesures')
plt.legend()
plt.xscale('log')
plt.grid()
plt.show()
