
import numpy as np
import matplotlib.pyplot as plt
from physique.modelisation import *
from physique.fonctions import *

f, Ue, Us, phi = np.loadtxt('ordre_2_wien.csv', delimiter=',', skiprows=1, unpack=True)
T = Us/Ue
G = 20*np.log10(T)

#modele = ajustement_ordre1_passe_bas_transmittance(f,T)
#modele = ajustement_ordre1_passe_bas_gain(f,G)
#modele = ajustement_ordre1_passe_bas_dephasage(f,phi)

#modele = ajustement_ordre1_passe_haut_transmittance(f,T)
#modele = ajustement_ordre1_passe_haut_gain(f,G)
#modele = ajustement_ordre1_passe_haut_dephasage(f,phi)

#modele = ajustement_ordre2_passe_bande_transmittance(f,T)
#modele = ajustement_ordre2_passe_bande_gain(f,G)
modele = ajustement_ordre2_passe_bande_dephasage(f,phi)
print(modele)

y = ordre2_passe_bande_dephasage(f, 3100, 1)

plt.plot(f, phi, '+r', label="Mesures")
plt.plot(f, y, '-b', label="Mesures")
modele.plot()
plt.xscale('log')
plt.legend()
plt.grid()
plt.show()
