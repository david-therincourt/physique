import numpy as np
import matplotlib.pyplot as plt
from physique.modelisation import ajustement_dephasage_ordre1_passe_haut
from mplcursors import cursor

f, Ue, Us, phi = np.loadtxt('bode_RC2.csv', delimiter=',', skiprows=1, unpack=True)

f0, line1 = ajustement_dephasage_ordre1_passe_haut(f, phi, plot_axes=plt, plot_nb_pts=500,return_line=True)
cursor([line1])
print(f0)

plt.plot(f, phi, '+', label="Mesures")
plt.legend()
plt.xscale('log')
plt.xlim(10,100E3)
plt.grid()

plt.show()