# Librairie Python pour les sciences physiques au lycée

## Installation

### A partir des dépôts de PyPi

Lancer dans un terminal :

	pip install physique

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
| ` ajustementLineaire(x, y)`                    | `a`                  | `y=ax​`                       |
| `ajustementAffine(x, y)`                       | `a`  et `b`          | `y=ax+b​`                     |
| `ajustementParabolique(x, y)`                  | `a` , `b` et  `c`    | `y=a x^2+bx+c​`               |
| `ajustementExponentielleCroissante(x, y)`      | `A`  et `tau`        | `y = A*(1-exp(-x/tau))`      |
| `ajustementExponentielleCroissanteX0(x, y)`    | `A` , `tau` et  `x0` | `y = A*(1-exp(-(x-x0)/tau))` |
| `ajustementExponentielleDecroissante(x, y)`    | `A`  et `tau`        | `y = A*exp(-x/tau)`          |
| `ajustementExponentielleDecroissanteX0(x, y) ` | `A` , `tau` et  `x0` | `y = A*exp(-(x-x0)/tau)`     |

#### Exemple :

```python
import numpy as np
import matplotlib.pyplot as plt
from physique import ajustementParabolique

x = np.array([0.003,0.141,0.275,0.410,0.554,0.686,0.820,0.958,1.089,1.227,1.359,1.490,1.599,1.705,1.801])
y = np.array([0.746,0.990,1.175,1.336,1.432,1.505,1.528,1.505,1.454,1.355,1.207,1.018,0.797,0.544,0.266])

[a, b, c] = ajustementParabolique(x, y)
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

* `importAvimeca3Txt(fichier)`  ou `importAvimeca3Txt(fichier, sep=';')`
* `importRegaviTxt(fichier)`  ou `importRegaviTxt(fichier, sep=';')` 

Le paramètre `sep` (séparateur de données) est optionnel. La tabulation (`sep='\t'`) est le séparateur par défaut.

#### Exemple :

```python
import matplotlib.pyplot as plt
from physique.csv import importAvimeca3Txt

t, x, y = importAvimeca3Txt('data1_avimeca3.txt')

plt.plot(x,y,'.')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.grid()
plt.title("Trajectoire d'un ballon")
plt.show()
```

Le fichier ` data.txt` est obtenu par l'exportation de données au format CSV dans le locigiel Aviméca3.

### Le module ` pyboard`

Module d’interfaçage d'une carte microcontrôleur (PyBoard, ESP32, Micro:bit, ...) fonctionnant sous MicroPython à partir d'un ordinateur sous Python par le port série (USB, Bluetooth, ...)

#### Exécuter un instruction MicroPython dans un programme Python

```python
from physique import Pyboard

pyboard = Pyboard("/dev/ttyACM0")
pyboard.enter_raw_repl()
pyboard.exec_('import pyb')
pyboard.exec_('pyb.LED(1).on()')
pyboard.exit_raw_repl()
```

#### Exécuter un fichier MicroPython dans un programme Python

* `execFile(nomFichier)`

  Exécute un programme MicroPython sur le microcontrôleur à partir d’un fichier `.py` présent sur l’ordinateur.

* `execFileToData(nomFichier) `

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
from physique import Pyboard

pyboard = Pyboard("/dev/ttyACM0")
x, y = pyboard.execFileToData("read_adc.py")

plt.plot(x,y,'r.')
plt.ylim(0,5000)
plt.show()
```

#### Exécuter un script MicroPython dans un programme Python

* `execScript(nomFichier)`

  Exécute un script Micropython sur le microcontrôleur dans un programme Python classique.

* `execScriptToData(nomFichier) `

  Exécute un script Micropython sur le microcontrôleur dans un programme Python classique. Retourne un tuple envoyé par une fonction `print(tuple)`  placée dans le programme Micropython.

##### Exemple :

Idem que l’exemple précédent mais dans un seul programme.

```python
import matplotlib.pyplot as plt
from physique import Pyboard

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

pyboard = Pyboard("/dev/ttyACM0")
x, y = pyboard.execScriptToData(script)

plt.plot(x,y,'r.')
plt.ylim(0,5000)
plt.show()
```



