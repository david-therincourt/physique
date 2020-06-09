from physique import Pyboard
import numpy as np
import matplotlib.pyplot as plt

script = """
from pyb import Pin, ADC, Timer
from time import sleep_ms
import array

f = 10000  # fréquence d'échantillonnage
nb = 2000  # nombre de points

adc = ADC(Pin('A0'))                           # Activation du CAN sur la broche A0
buf = array.array("h", [0 for i in range(nb)]) # h = signed short (entier sur 2 octets)
tim = Timer(6, freq=f)                         # Paramétrage du timer du CAN
# sleep_ms(3000)
adc.read_timed(buf, tim)     # Lancement des mesures

# Mise en forme des données
x = [i*1/f for i in range(nb)]
y = [val for val in buf]

# transmission des données
data = x, y    # Tuple de données
print(data)    # Affichage du tuple dans le REPL
"""

feather = Pyboard("/dev/ttyACM0")
x, y = feather.execScriptToData(script)

t = np.array(x)
u = np.array(y)

plt.subplot(2,1,1)
plt.plot(t,u,'r')
plt.grid()
plt.ylim(0,4000)

plt.subplot(2,1,2)
plt.magnitude_spectrum(u, Fs=20000)
#plt.ylim(0,500)
plt.xlim(0,1000)

plt.show()
