from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
from physique.modelisation import ajustement_transmittance_ordre1_passe_bas

f, Ue, Us, phi = np.loadtxt('bode_RC1.csv', delimiter=',', skiprows=1, unpack=True)

T = Us/Ue

T0, f0 = ajustement_transmittance_ordre1_passe_bas(f, T, plot_ax=plt)


plt.plot(f, T, '+', label="Mesures")
plt.legend()
plt.xscale('log')
plt.xlim(10,100E3)
plt.grid()

plt.show()