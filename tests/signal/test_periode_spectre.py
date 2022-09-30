import numpy as np
import matplotlib.pyplot as plt
from physique import load_oscillo_csv, periode, spectre_RMS
from mplcursors import cursor

fig, (axes1, axes2) = plt.subplots(2, 1)

t, u = load_oscillo_csv('scope_periode.csv')
u = u - 1.5

T = periode(t, u, draw_period_ax=axes1, draw_period_start=0)
freq = 1/T

f, A = spectre_RMS(t, u, T)

plt.subplot(211)
plt.plot(t, u)
plt.grid()

plt.subplot(212)
plt.stem(f, A)
cursor()
plt.xlim(0, 2000)
plt.grid()
plt.show()