from physique import Pyboard
feather = Pyboard("/dev/ttyACM0")
reponse = feather.execFile("hello.py")
print(reponse)
