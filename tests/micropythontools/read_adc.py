from pyb import Pin, ADC
from time import sleep_ms

adc = ADC(Pin('X1'))     # Broche X1 en entrée analogique

x, y = [], []            # Tableaux vides au départ

for i in range(10):      # Mesures
    x.append(i)
    y.append(adc.read()) # Lecture sur CAN
    sleep_ms(500)        # attendre 500 ms

data = x, y              # Tuple de données
print(data)              # Envoie des données
