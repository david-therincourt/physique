# Programme MicroPython pour Pyboard
# Charge d'un condensateur à travers une résistance
# R = 100k et C = 220 nF

from pyb import Pin, ADC, Timer
from time import sleep_ms
import array
T = 1    # millisecond
f = 1000/T
nb = 50



pinX1 = Pin('X1', Pin.OUT)   # Alimentation du circuit RC
pinX2  = Pin('X2')           # Tension condensateur
adc = ADC(pinX2)             # Activation du CAN
buf = array.array("h", nb * [0x7FFF]) # h = signed short (int 2 octets)
tim = Timer(6, freq=f)         # create a timer running at 10Hz


pinX1.low()                  # Décharge du condensateur
sleep_ms(1000)               # Attendre 2 s
pinX1.high()                 # Début de la charge

adc.read_timed(buf, tim)     # Mesures

# Données
x = [i*1/f*1000 for i in range(nb)]
y = [val for val in buf]

data = x, y
print(data)
