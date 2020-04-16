# Programme MicroPython pour Pyboard
# Charge d'un condensateur à travers une résistance
# R = 100k et C = 220 nF

from pyb import Pin, ADC, Timer
from time import sleep_ms
import array

T = 2       # période en milliseconde
f = 10**3/T  # fréquence d'échantillonnage
nb = 50     # nombre de points

pinX1 = Pin('X1', Pin.OUT)   # entrée du circuit RC
pinX2  = Pin('X2')           # broche du condensateur

adc = ADC(pinX2)                               # Activation du CAN sur la broche X2
buf = array.array("h", [0 for i in range(nb)]) # h = signed short (entier sur 2 octets)
tim = Timer(6, freq=f)                         # Paramétrage du timer du CAN


pinX1.low()                  # Décharge du condensateur X1 = 0V
sleep_ms(1000)               # Attendre xxxx ms
pinX1.high()                 # Début de la charge X1 = Vcc

adc.read_timed(buf, tim)     # Lancement des mesures

# Mise en forme des données
x = [i*1/f*1000 for i in range(nb)]
y = [val for val in buf]

# transmission des données
data = x, y    # Tuple de données
print(data)    # Affichage du tuple dans le REPL
