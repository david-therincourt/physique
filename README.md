# Librairie Python pour les sciences physiques au lycée

## Installation

### A partir des dépôts de PyPi

Lancer dans un terminal :

	pip install physique

Dépendance à installer :

```python
pip install pyserial
```



### A partir de l'archive de la bibliothèque

Télécharger [ici](https://pypi.org/project/physique/#files) le fichier `physique-x.x.whl`. Les caractères `x` sont à remplacer par les numéros de version.

Dans une console Python dans le même répertoire que l'archive et lancer la commande suivante :

	pip install physique-x.x.whl

## Utilisation

### Le module `modelisation`

Fonctions pour réaliser une modélisation d'une courbe du type `y=f(x)`.

#### Fonctions disponibles

| Fonctions                                      | Valeurs de retour    | Type de fonction modélisée   |
| ---------------------------------------------- | -------------------- | ---------------------------- |
| ` ajustement_lineaire(x, y)`                    | `a`                  | `y=ax​`                       |
| `ajustement_affine(x, y)`                       | `a`  et `b`          | `y=ax+b​`                     |
| `ajustement_parabolique(x, y)`                  | `a` , `b` et  `c`    | `y=a x^2+bx+c​`               |
| `ajustement_exponentielle_croissante(x, y)`      | `A`  et `tau`        | `y = A*(1-exp(-x/tau))`      |
| `ajustement_exponentielle_croissante_x0(x, y)`    | `A` , `tau` et  `x0` | `y = A*(1-exp(-(x-x0)/tau))` |
| `ajustement_exponentielle_decroissante(x, y)`    | `A`  et `tau`        | `y = A*exp(-x/tau)`          |
| `ajustement_exponentielle_decroissante_x0(x, y) ` | `A` , `tau` et  `x0` | `y = A*exp(-(x-x0)/tau)`     |

#### Exemple :

```python
import numpy as np
import matplotlib.pyplot as plt
from physique.modelisation import ajustement_parabolique

x = np.array([0.003,0.141,0.275,0.410,0.554,0.686,0.820,0.958,1.089,1.227,1.359,1.490,1.599,1.705,1.801])
y = np.array([0.746,0.990,1.175,1.336,1.432,1.505,1.528,1.505,1.454,1.355,1.207,1.018,0.797,0.544,0.266])

[a, b, c] = ajustement_parabolique(x, y)
print(a, b, c)

x_mod = np.linspace(0,max(x),50)
y_mod = a*x_mod**2 + b*x_mod + c

plt.plot(x_mod, y_mod, '-')
plt.plot(x, y, 'x')
plt.show()
```

### Le module `CSV`

Modules d'importation de tableau de données au format CSV à partir des logiciels Aviméca3, Regavi, ...

#### Quelques fonctions disponibles

* `import_avimeca3_txt(fichier)`  ou `import_avimeca3_txt(fichier, sep=';')`
* `import_regavi_txt(fichier)`  ou `import_regavi_txt(fichier, sep=';')` 

Le paramètre `sep` (séparateur de données) est optionnel. La tabulation (`sep='\t'`) est le séparateur par défaut.

#### Exemple :

```python
import matplotlib.pyplot as plt
from physique.csv import import_avimeca3_txt

t, x, y = import_avimeca3_txt('data1_avimeca3.txt')

plt.plot(x,y,'.')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.grid()
plt.title("Trajectoire d'un ballon")
plt.show()
```

Le fichier ` data.txt` est obtenu par l'exportation de données au format CSV dans le locigiel Aviméca3.

### Le module ` pyboard`

Module d’interfaçage d'une carte microcontrôleur (PyBoard, ESP32, Micro:bit, ...) fonctionnant avec MicroPython à partir d'un ordinateur sous Python classique par le port série (USB, Bluetooth, ...) ou par le réseau.

#### Exécuter des instructions MicroPython dans un programme Python

```python
from physique.pyboard import Pyboard

pyboard = Pyboard("COM3") # Port série de la carte ("/dev/ttyACM0" pour linux)
pyboard.enter_raw_repl()
pyboard.exec('import pyb')       # Exécute une instruction MicroPython
pyboard.exec('pyb.LED(1).on()')  # Exécute une autre instruction MicroPython
pyboard.exit_raw_repl()
```

Ou plusieurs instructions à la fois :

```python
from physique.pyboard import Pyboard
from time import sleep

pyboard = Pyboard("COM3") # Port série de la carte ("/dev/ttyACM0" pour linux)
pyboard.enter_raw_repl()  # Entre dans le mode REPL

pyboard.exec("""          # Execute plusieurs instructions
from pyb import LED
led = LED(1)
""")
for i in range(10):
    pyboard.exec("led.toggle()")
    sleep(1)
   
pyboard.exit_raw_repl()   # Sort du mode REPL
```



#### Exécuter un fichier MicroPython dans un programme Python

* `exec_file(nomFichier)`

  Exécute un programme MicroPython sur le microcontrôleur à partir d’un fichier `.py` présent sur l’ordinateur.

* `exec_file_to_data(nomFichier) `

  Exécute un programme MicroPython sur le microcontrôleur à partir d’un fichier `.py` présent sur l’ordinateur. Retourne un tuple envoyé par une fonction `print(tuple)`  placée dans le programme MicroPython.

##### Exemple :

Programme MicroPython `read_adc.py` pour carte PyBoard (lecture sur entrée analogique) :

```python
from pyb import Pin, ADC
from time import sleep_ms
adc = ADC(Pin('A0'))     # Broche X1 ou A0 en entrée analogique
x, y = [], []            # Tableaux vides au départ
for i in range(10):      # Mesures
    x.append(i)
    y.append(adc.read()) # Lecture sur CAN
    sleep_ms(500)        # attendre 500 ms
data = x, y              # Tuple de données
print(data)              # Envoie des données
```

Programme Python sur l'ordinateur dans le même répertoire que le programme MicroPython :

```python
import matplotlib.pyplot as plt
from physique.pyboard import Pyboard

pyboard = Pyboard("COM3") # Port série de la carte ("/dev/ttyACM0" pour linux)
x, y = pyboard.exec_file_to_data("read_adc.py")

plt.plot(x,y,'r.')
plt.ylim(0,5000)
plt.show()
```

#### Exécuter un script MicroPython dans un programme Python

* `exec_script(nomFichier)`

  Exécute un script Micropython sur le microcontrôleur dans un programme Python classique.

* `exec_script_to_data(nomFichier) `

  Exécute un script Micropython sur le microcontrôleur dans un programme Python classique. Retourne un tuple envoyé par une fonction `print(tuple)`  placée dans le programme Micropython.

##### Exemple :

Idem que l’exemple précédent mais dans un seul programme.

```python
import matplotlib.pyplot as plt
from physique.pyboard import Pyboard

script = """
from pyb import Pin, ADC
from time import sleep_ms
adc = ADC(Pin('A0'))     # Broche X1 ou A0 en entrée analogique
x, y = [], []            # Tableaux vides au départ
for i in range(10):      # Mesures
    x.append(i)
    y.append(adc.read()) # Lecture sur CAN
    sleep_ms(500)        # attendre 500 ms
data = x, y              # Tuple de données
print(data)              # Envoie des données
"""

pyboard = Pyboard("COM3") # Port série de la carte ("/dev/ttyACM0" pour linux)
x, y = pyboard.exec_script_to_data(script)

plt.plot(x,y,'r.')
plt.ylim(0,5000)
plt.show()
```



