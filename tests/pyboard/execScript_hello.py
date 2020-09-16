from physique import Pyboard

feather = Pyboard("/dev/ttyACM0")

reponse = feather.exec_script("""
print("Hello")
print("MicroPython")
""")

print(reponse)
