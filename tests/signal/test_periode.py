import numpy as np
import matplotlib.pyplot as plt
from physique import load_oscillo_csv, periode

t, u = load_oscillo_csv('scope_periode.csv')
t=t*1000

T = periode(t, u, draw_period_axes=plt, draw_period_start=0)

plt.plot(t, u)

plt.grid()
plt.show()