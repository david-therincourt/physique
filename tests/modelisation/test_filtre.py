
import numpy as np
import matplotlib.pyplot as plt
from physique.modelisation import *
from physique.fonctions import *

f, Ue, Us, phi = np.loadtxt('ordre_1a.csv', delimiter=',', skiprows=1, unpack=True)
T = Us/Ue
G = 20*np.log10(T)

modele = ajustement_ordre1_passe_bas_transmittance(f,T)
#modele = ajustement_ordre1_passe_bas_gain(f,G)
#modele = ajustement_ordre1_passe_bas_dephasage(f,phi)

#modele = ajustement_ordre1_passe_haut_transmittance(f,T)
#modele = ajustement_ordre1_passe_haut_gain(f,G)
#modele = ajustement_ordre1_passe_haut_dephasage(f,phi)

#modele = ajustement_ordre2_passe_bande_transmittance(f,T)
#modele = ajustement_ordre2_passe_bande_gain(f,G)
#modele = ajustement_ordre2_passe_bande_dephasage(f,phi)
#modele.set_xmin(10)
#modele.set_xmax(1e6)
modele.set_print_error(True)
print(modele)




plt.plot(f, T, '+r', label="Mesures")
modele.plot()
plt.xscale('log')
plt.legend()
plt.grid()
plt.show()
