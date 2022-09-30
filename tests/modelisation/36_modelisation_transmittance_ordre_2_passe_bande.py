import numpy as np
import matplotlib.pyplot as plt
from physique.modelisation import ajustement_transmittance_ordre2_passe_bande

### IMPORTATION ###
f, Us = np.loadtxt('wien.csv', delimiter=',', skiprows=1, unpack=True)

### CACLCULS ###
Ue = 4.44
T = Us/Ue


### MODELISATION ###
T0, f0, m = ajustement_transmittance_ordre2_passe_bande(f, T, plot_ax=plt)
print("T0 = {} \t f0 = {} \t m = {}".format(T0, f0, m))


### COURBE ###
plt.plot(f, T, '+')
plt.legend()
plt.xscale('log')
plt.grid()
plt.show()
