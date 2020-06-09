from physique import Pyboard

programme = """
from pyb import LED
from time import sleep_ms

for i in range(10):
    LED(1).toggle()
    sleep_ms(500)
"""

feather = Pyboard("/dev/ttyACM0")
feather.execScript(programme)
