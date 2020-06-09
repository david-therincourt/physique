from physique import Pyboard

feather = Pyboard("/dev/ttyACM0")

reponse = feather.execScript("""
print("Hello")
print("MicroPython")
""")

print(reponse)
