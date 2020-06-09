from physique import Pyboard

programme = """
from pyb import Pin, ADC
from time import sleep_ms

adc = ADC(Pin("A0"))

x = []
y = []

for i in range(10):
    x.append(i)
    y.append(adc.read())
    sleep_ms(100)

print((x, y))
"""

feather = Pyboard("/dev/ttyACM0")
x, y = feather.execScriptToData(programme)

print("x = ", x)
print("y = ", y)
