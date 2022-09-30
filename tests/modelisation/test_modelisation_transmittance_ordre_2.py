import numpy as np
import matplotlib.pyplot as plt
from physique.modelisation import *

### IMPORTATION ###
f, Us = np.loadtxt('ordre2.csv', delimiter=',', skiprows=1, unpack=True)

### CACLCULS ###
Ue = 4.7
T = Us/Ue
G = 20*np.log10(T)

### MODELISATION ###
T0, f0, m = ajustement_transmittance_ordre2_passe_bas(f, T)
print("T0 = {} \t f0 = {} \t m = {}".format(T0, f0, m))

f_m = np.logspace(2, 4, num = 100)
T_m = transmittance_ordre2_passe_bas(f_m, T0, f0, m)
G_m = 20*np.log10(T_m)

### COURBE ###
plt.plot(f_m, G_m, '-')
plt.plot(f, G, '+')
plt.xscale('log')
plt.grid()
plt.show()
