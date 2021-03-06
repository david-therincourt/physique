from physique import Pyboard
import numpy as np
import matplotlib.pyplot as plt

script = """
from pyb import Pin, ADC, Timer, delay

import array

f = 20000  # fréquence d'échantillonnage
nb = 2000  # nombre de points

adc = ADC(Pin('A2'))                           # Activation du CAN sur la broche A0
buf = array.array("h", [0]*nb) # h = signed short (entier sur 2 octets)
tim = Timer(6, freq=f)                         # Paramétrage du timer du CAN
adc.read_timed(buf, tim)     # Lancement des mesures

# Mise en forme des données
f = tim.freq()
x = [i*1/f for i in range(nb)]
y = [val for val in buf]

# transmission des données
data = x, y    # Tuple de données
print(data)    # Affichage du tuple dans le REPL
"""

feather = Pyboard("/dev/ttyACM0")
x, y = feather.exec_script_to_data(script)

t = np.array(x)
u = np.array(y)

plt.subplot(2,1,1)
plt.plot(t,u,'r')
plt.grid()
#plt.ylim(0,100)

plt.subplot(2,1,2)
plt.magnitude_spectrum(u, Fs=20000)
plt.ylim(0,50)
plt.xlim(0,1000)

plt.show()
