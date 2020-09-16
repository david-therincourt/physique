from physique import Pyboard
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft

script = """
from pyb import Pin, ADC, Timer, delay

import array

f = 20000  # fréquence d'échantillonnage
nb = 1000  # nombre de points

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
rate = 20000

plt.subplot(2,1,1)
plt.plot(t,u,'r')
plt.grid()
#plt.ylim(0,4000)

plt.subplot(2,1,2)
spectre = np.absolute(fft(y))
#spectre = spectre/spectre.max()
n = spectre.size
freq = np.arange(n)*1.0/n*rate
plt.vlines(freq[1:-1],[0],spectre[1:-1],'r')
plt.xlabel('f (Hz)')
plt.ylabel('A')
#plt.axis([0,0.5*rate,0,1])

plt.show()
