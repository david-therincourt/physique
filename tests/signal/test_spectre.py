import numpy as np
import matplotlib.pyplot as plt
from physique import load_oscillo_csv, spectre_amplitude, spectre_RMS, spectre_RMS_dBV

fig, (axes1, axes2) = plt.subplots(2,1)

t, u = load_oscillo_csv('scope_carre.csv')

f = 250
T = 1/f

f, A = spectre_amplitude(t, u, T, tmin=2E-3, plot_period_axes=axes1)

plt.subplot(211)
plt.plot(t, u)
plt.grid()

plt.subplot(212)
plt.stem(f, A, basefmt="C7", bottom=0)
plt.xlim(-250, 3000)
plt.grid()

plt.show()