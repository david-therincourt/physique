import matplotlib.pyplot as plt
from physique.csv import load_oscillo_csv
from physique.signal import periode

t, u = load_oscillo_csv('scope_periode.csv')
t=t*1000

T = periode(u, t, draw_period_ax=plt, draw_period_start=0)
print(T)

plt.plot(t, u)

plt.grid()
plt.show()