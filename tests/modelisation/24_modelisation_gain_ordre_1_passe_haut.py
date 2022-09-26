#from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
from physique.modelisation import ajustement_gain_ordre1_passe_haut

f, Ue, Us, phi = np.loadtxt('bode_RC2.csv', delimiter=',', skiprows=1, unpack=True)

G = 20*np.log10(Us/Ue)

G0, f0 = ajustement_gain_ordre1_passe_haut(f, G, plot_axes=plt)
print(G0, f0)

plt.plot(f, G, '+', label="Mesures")
plt.legend()
plt.xscale('log')
plt.xlim(10,100E3)
plt.grid()

plt.show()